#!/usr/bin/env python3
"""Plan OSGi/Maven builds and generate dependency graph reports."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict, deque
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
REPOSITORY_DIR = PROJECT_DIR.parent


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def child_text(element: ET.Element, name: str) -> str | None:
    return next((child.text.strip() for child in element if local_name(child.tag) == name and child.text), None)


def read_xml(path: Path) -> ET.Element:
    try:
        return ET.parse(path).getroot()
    except (ET.ParseError, OSError) as error:
        raise RuntimeError(f"Unable to parse {path.relative_to(PROJECT_DIR)}: {error}") from error


def parse_manifest(path: Path) -> dict[str, str]:
    headers: dict[str, str] = {}
    current: str | None = None
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        raise RuntimeError(f"Unable to read {path.relative_to(PROJECT_DIR)}: {error}") from error

    for line in lines:
        if line.startswith(" ") and current:
            headers[current] += line[1:]
        elif ":" in line:
            current, value = line.split(":", 1)
            headers[current] = value.strip()
        else:
            current = None
    return headers


def clauses(header: str) -> list[str]:
    return [clause.strip() for clause in header.split(",") if clause.strip()]


def bundle_id(value: str) -> str:
    return value.split(";", 1)[0].strip()


def parse_projects(root: ET.Element, parent: str = ".") -> tuple[dict[str, dict], dict[str, list[str]]]:
    projects: dict[str, dict] = {}
    children_by_product: dict[str, list[str]] = defaultdict(list)

    def visit(pom: Path, product: str | None) -> None:
        relative = pom.parent.relative_to(PROJECT_DIR).as_posix()
        relative = "." if relative == "." else relative
        element = read_xml(pom)
        artifact = child_text(element, "artifactId") or relative
        group = child_text(element, "groupId")
        if not group:
            parent_element = next((item for item in element if local_name(item.tag) == "parent"), None)
            group = child_text(parent_element, "groupId") if parent_element is not None else None
        projects[relative] = {"artifactId": artifact, "groupId": group, "product": product}

        module_names = [
            item.text.strip()
            for item in element.iter()
            if local_name(item.tag) == "module" and item.text and item is not element
        ]
        for module_name in module_names:
            module_pom = (pom.parent / module_name / "pom.xml").resolve()
            if not module_pom.is_file():
                raise RuntimeError(f"Maven module has no POM: {module_pom}")
            module_relative = module_pom.parent.relative_to(PROJECT_DIR).as_posix()
            module_product = product or module_name
            children_by_product[module_product].append(module_relative)
            visit(module_pom, module_product)

    root_pom = PROJECT_DIR / "pom.xml"
    for module in [
        item.text.strip()
        for item in root.iter()
        if local_name(item.tag) == "module" and item.text
    ]:
        visit(root_pom.parent / module / "pom.xml", module)
    return projects, children_by_product


def discover_graph() -> tuple[list[str], dict[str, dict], list[dict], list[dict]]:
    root = read_xml(PROJECT_DIR / "pom.xml")
    products = [
        item.text.strip()
        for item in root.iter()
        if local_name(item.tag) == "module" and item.text
    ]
    projects, product_projects = parse_projects(root)
    bundles: dict[str, dict] = {}
    package_owners: dict[str, str] = {}
    features: dict[str, dict] = {}

    for path in sorted(PROJECT_DIR.glob("**/META-INF/MANIFEST.MF")):
        headers = parse_manifest(path)
        symbolic_name = bundle_id(headers.get("Bundle-SymbolicName", ""))
        if not symbolic_name:
            continue
        product = path.relative_to(PROJECT_DIR).parts[0]
        exports = [bundle_id(item) for item in clauses(headers.get("Export-Package", ""))]
        bundle = {
            "id": symbolic_name,
            "product": product,
            "path": path.relative_to(PROJECT_DIR).as_posix(),
            "headers": headers,
            "exports": exports,
        }
        bundles[symbolic_name] = bundle
        for package in exports:
            package_owners[package] = symbolic_name

    for path in sorted(PROJECT_DIR.glob("**/feature.xml")):
        element = read_xml(path)
        feature_id = element.attrib.get("id")
        if feature_id:
            features[feature_id] = {
                "id": feature_id,
                "product": path.relative_to(PROJECT_DIR).parts[0],
                "path": path.relative_to(PROJECT_DIR).as_posix(),
                "xml": element,
            }

    osgi_edges: list[dict] = []
    product_dependencies: dict[str, set[str]] = {product: set() for product in products}
    for bundle in bundles.values():
        headers = bundle["headers"]
        for package_clause in clauses(headers.get("Import-Package", "")):
            package = bundle_id(package_clause)
            provider_id = package_owners.get(package)
            if provider_id:
                provider = bundles[provider_id]
                if provider_id != bundle["id"]:
                    osgi_edges.append({
                        "from": bundle["id"],
                        "to": provider_id,
                        "kind": "imports-package",
                        "detail": package,
                        "fromProduct": bundle["product"],
                        "toProduct": provider["product"],
                    })
                    if provider["product"] != bundle["product"]:
                        product_dependencies[bundle["product"]].add(provider["product"])
        for required_clause in clauses(headers.get("Require-Bundle", "")):
            required_id = bundle_id(required_clause)
            provider = bundles.get(required_id)
            if provider:
                osgi_edges.append({
                    "from": bundle["id"],
                    "to": required_id,
                    "kind": "requires-bundle",
                    "detail": required_id,
                    "fromProduct": bundle["product"],
                    "toProduct": provider["product"],
                })
                if provider["product"] != bundle["product"]:
                    product_dependencies[bundle["product"]].add(provider["product"])

    feature_edges: list[dict] = []
    for feature in features.values():
        for item in feature["xml"].iter():
            name = local_name(item.tag)
            if name == "import" and item.attrib.get("feature") in features:
                target = features[item.attrib["feature"]]
                feature_edges.append({
                    "from": feature["id"],
                    "to": target["id"],
                    "kind": "requires-feature",
                    "fromProduct": feature["product"],
                    "toProduct": target["product"],
                })
                if feature["product"] != target["product"]:
                    product_dependencies[feature["product"]].add(target["product"])
            elif name == "plugin":
                plugin_id = item.attrib.get("id")
                plugin = bundles.get(plugin_id or "")
                if plugin:
                    feature_edges.append({
                        "from": feature["id"],
                        "to": plugin_id,
                        "kind": "contains-bundle",
                        "fromProduct": feature["product"],
                        "toProduct": plugin["product"],
                    })

    artifact_projects: dict[str, str] = {}
    for project_path, project in projects.items():
        artifact_projects[project["artifactId"]] = project_path
    maven_edges: list[dict] = []
    for project_path, project in projects.items():
        if project_path == ".":
            continue
        pom = PROJECT_DIR / project_path / "pom.xml"
        element = read_xml(pom)
        for dependency in (node for node in element.iter() if local_name(node.tag) == "dependency"):
            artifact = child_text(dependency, "artifactId")
            dependency_path = artifact_projects.get(artifact or "")
            if dependency_path and dependency_path != project_path:
                maven_edges.append({
                    "from": project_path,
                    "to": dependency_path,
                    "kind": "maven-dependency",
                })
    for product, project_paths in product_projects.items():
        product_path = product
        for project_path in project_paths:
            if project_path != product_path:
                maven_edges.append({
                    "from": product_path,
                    "to": project_path,
                    "kind": "contains-module",
                })

    return products, {
        "projects": projects,
        "productProjects": product_projects,
        "bundles": bundles,
        "features": features,
        "productDependencies": product_dependencies,
    }, maven_edges, osgi_edges + feature_edges


def changed_paths(base: str | None) -> list[str]:
    if not base:
        return []
    try:
        result = subprocess.run(
            ["git", "-C", str(REPOSITORY_DIR), "diff", "--name-only", "--diff-filter=ACMRT", f"{base}...HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"Could not calculate changes from {base!r}; planning a full build ({error}).", file=sys.stderr)
        return []
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def select_products(products: list[str], mode: str, paths: list[str], dependencies: dict[str, set[str]]) -> tuple[list[str], list[str], dict[str, list[str]]]:
    if mode == "full":
        return products, products, {}

    changed: set[str] = set()
    for path in paths:
        normalized = path.replace("\\", "/")
        if normalized == "osgi-workshop/pom.xml":
            return products, products, {}
        if normalized.startswith("osgi-workshop/"):
            remainder = normalized.removeprefix("osgi-workshop/")
            first = remainder.split("/", 1)[0]
            if first in products:
                changed.add(first)
            else:
                return products, products, {}
        else:
            return products, products, {}
    if not changed:
        print("No changed project paths were detected; planning a full build.")
        return products, products, {}

    reverse_dependencies: dict[str, set[str]] = defaultdict(set)
    for consumer, prerequisites in dependencies.items():
        for prerequisite in prerequisites:
            reverse_dependencies[prerequisite].add(consumer)
    impacted = set(changed)
    paths_by_change: dict[str, list[str]] = {}
    for changed_product in sorted(changed):
        queue = deque([(changed_product, [changed_product])])
        seen_paths: set[str] = set()
        while queue:
            current, chain = queue.popleft()
            for dependent in sorted(reverse_dependencies[current]):
                if dependent in chain:
                    continue
                impacted.add(dependent)
                dependency_path = " -> ".join(chain + [dependent])
                if dependency_path not in seen_paths:
                    seen_paths.add(dependency_path)
                    paths_by_change.setdefault(changed_product, []).append(dependency_path)
                queue.append((dependent, chain + [dependent]))

    build_products = set(impacted)
    pending = list(impacted)
    while pending:
        current = pending.pop()
        for prerequisite in dependencies[current]:
            if prerequisite not in build_products:
                build_products.add(prerequisite)
                pending.append(prerequisite)

    ordered: list[str] = []
    visiting: set[str] = set()
    visited_products: set[str] = set()

    def visit(product: str) -> None:
        if product in visited_products:
            return
        if product in visiting:
            raise RuntimeError(f"Circular product dependency detected at {product}")
        visiting.add(product)
        for prerequisite in sorted(dependencies[product]):
            if prerequisite in build_products:
                visit(prerequisite)
        visiting.remove(product)
        visited_products.add(product)
        ordered.append(product)

    for product in products:
        if product in build_products:
            visit(product)
    return sorted(changed), ordered, paths_by_change


def write_reports(
    output_dir: Path,
    products: list[str],
    graph: dict,
    maven_edges: list[dict],
    osgi_edges: list[dict],
    mode: str,
    changed: list[str],
    build_products: list[str],
    paths_by_change: dict[str, list[str]],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    product_dependencies = graph["productDependencies"]
    report = {
        "mode": mode,
        "changedProducts": changed,
        "selectedProducts": build_products,
        "dependencyPaths": paths_by_change,
        "maven": {
            "projects": graph["projects"],
            "edges": maven_edges,
        },
        "osgi": {
            "bundles": {
                key: {"product": value["product"], "path": value["path"], "exports": value["exports"]}
                for key, value in graph["bundles"].items()
            },
            "features": {
                key: {"product": value["product"], "path": value["path"]}
                for key, value in graph["features"].items()
            },
            "edges": osgi_edges,
        },
        "productDependencies": {
            key: sorted(value) for key, value in product_dependencies.items()
        },
    }
    (output_dir / "dependency-graph.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    selected = set(build_products)
    for scenario in ("full", "changed"):
        products_to_show = set(products)
        lines = ["flowchart LR", "  subgraph Maven[\"Maven reactor modules\"]"]
        for project_path, project in graph["projects"].items():
            if project_path == "." or project["product"] not in products_to_show:
                continue
            node_id = "m_" + re.sub(r"[^A-Za-z0-9_]", "_", project_path)
            lines.append(f'    {node_id}["{project_path}"]')
        for edge in maven_edges:
            source = graph["projects"].get(edge["from"], {})
            target = graph["projects"].get(edge["to"], {})
            if source.get("product") not in products_to_show or target.get("product") not in products_to_show:
                continue
            source_id = "m_" + re.sub(r"[^A-Za-z0-9_]", "_", edge["from"])
            target_id = "m_" + re.sub(r"[^A-Za-z0-9_]", "_", edge["to"])
            arrow = "-.->" if edge["kind"] == "maven-dependency" else "-->"
            lines.append(f'    {source_id} {arrow}|{edge["kind"]}| {target_id}')
        lines.append("  end")
        if scenario == "changed":
            lines.append('  subgraph Impact["Changed-product impact paths"]')
            for product in products:
                label = f"{product} (selected)" if product in selected else product
                lines.append(f'    p_{product}["{label}"]')
            for consumer, prerequisites in product_dependencies.items():
                for prerequisite in sorted(prerequisites):
                    lines.append(f"    p_{prerequisite} -->|dependency| p_{consumer}")
            for product in changed:
                lines.append(f"    p_{product}:::changed")
            lines.append("  end")
        lines.append('  subgraph OSGi["OSGi bundles and features"]')
        included_bundles = {
            key: value for key, value in graph["bundles"].items()
            if value["product"] in products_to_show
        }
        included_features = {
            key: value for key, value in graph["features"].items()
            if value["product"] in products_to_show
        }
        for bundle_id_value, bundle in included_bundles.items():
            node_id = "o_" + re.sub(r"[^A-Za-z0-9_]", "_", bundle_id_value)
            lines.append(f'    {node_id}["{bundle_id_value}"]')
        for feature_id, feature in included_features.items():
            node_id = "f_" + re.sub(r"[^A-Za-z0-9_]", "_", feature_id)
            lines.append(f'    {node_id}(["{feature_id}"])')
        for edge in osgi_edges:
            if edge["fromProduct"] not in products_to_show or edge["toProduct"] not in products_to_show:
                continue
            source_prefix = "f_" if edge["from"] in graph["features"] else "o_"
            target_prefix = "f_" if edge["to"] in graph["features"] else "o_"
            source_id = source_prefix + re.sub(r"[^A-Za-z0-9_]", "_", edge["from"])
            target_id = target_prefix + re.sub(r"[^A-Za-z0-9_]", "_", edge["to"])
            lines.append(f'    {source_id} -->|{edge["kind"]}| {target_id}')
        lines.append("  end")
        if scenario == "changed":
            lines.append("  classDef selected fill:#d1fae5,stroke:#059669,stroke-width:2px")
            lines.append("  classDef changed fill:#fef3c7,stroke:#d97706,stroke-width:3px")
            for product in sorted(selected):
                for project_path, project in graph["projects"].items():
                    if project["product"] == product:
                        node_id = "m_" + re.sub(r"[^A-Za-z0-9_]", "_", project_path)
                        lines.append(f"  class {node_id} selected")
                for bundle_id_value, bundle in included_bundles.items():
                    if bundle["product"] == product:
                        node_id = "o_" + re.sub(r"[^A-Za-z0-9_]", "_", bundle_id_value)
                        lines.append(f"  class {node_id} selected")
                for feature_id, feature in included_features.items():
                    if feature["product"] == product:
                        node_id = "f_" + re.sub(r"[^A-Za-z0-9_]", "_", feature_id)
                        lines.append(f"  class {node_id} selected")
            for product in changed:
                lines.append(f"  class p_{product} changed")
        (output_dir / f"dependency-graph-{scenario}.mmd").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("full", "changed"), default="full")
    parser.add_argument("--base", help="Git ref used to discover changed files.")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_DIR / "build-reports")
    parser.add_argument("--changed-path", action="append", default=[], help="Changed path (repeatable; intended for local use/testing).")
    args = parser.parse_args()

    products, graph, maven_edges, osgi_edges = discover_graph()
    paths = args.changed_path or changed_paths(args.base)
    changed, build_products, dependency_paths = select_products(
        products, args.mode, paths, graph["productDependencies"]
    )
    build_products = build_products if args.mode == "changed" else products
    if args.mode == "full":
        changed = []
        dependency_paths = {}

    print(f"Build scenario: {args.mode}")
    print(f"Changed paths: {', '.join(paths) if paths else '(none; full-build fallback if needed)'}")
    print(f"Changed products: {', '.join(changed) if changed else '(none)'}")
    for product, chains in dependency_paths.items():
        for chain in chains:
            print(f"Dependency impact: {chain}")
    print(f"Selected products (dependency order): {', '.join(build_products)}")

    write_reports(
        args.output_dir, products, graph, maven_edges, osgi_edges,
        args.mode, changed, build_products, dependency_paths,
    )

    selectors = []
    if args.mode == "changed":
        for product in build_products:
            selectors.append(product)
            selectors.extend(graph["productProjects"].get(product, []))
        selectors = list(dict.fromkeys(selectors))
        print(f"Selected Maven reactor projects: {', '.join(selectors)}")
    outputs = {
        "changed_products": ",".join(changed),
        "selected_products": ",".join(build_products),
        "maven_projects": ",".join(selectors),
        "build_required": "true" if build_products else "false",
    }
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as stream:
            for key, value in outputs.items():
                stream.write(f"{key}={value}\n")
    print(f"Dependency reports written to {args.output_dir}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(f"Build planning failed: {error}", file=sys.stderr)
        raise SystemExit(1)
