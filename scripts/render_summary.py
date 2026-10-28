#!/usr/bin/env python3
"""Render dependency graph reports as HTML and/or a GitHub Actions step summary."""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path
from urllib.parse import urlparse


PROJECT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_REPORT_DIR = PROJECT_DIR / "build-reports"


def read_report(report_dir: Path) -> tuple[dict, dict[str, str]]:
    report = json.loads((report_dir / "dependency-graph.json").read_text(encoding="utf-8"))
    graphs = {
        scenario: (report_dir / f"dependency-graph-{scenario}.mmd").read_text(encoding="utf-8").strip()
        for scenario in ("full", "changed")
    }
    return report, graphs


def render_markdown(report: dict, graphs: dict[str, str], artifact_url: str | None) -> str:
    mode = report["mode"]
    changed = report.get("changedProducts", [])
    selected = report.get("selectedProducts", [])
    paths = report.get("dependencyPaths", {})

    lines = [
        "## Dependency graph",
        "",
        f"**Build scenario:** `{mode}`",
        f"**Changed products:** {', '.join(f'`{product}`' for product in changed) or 'None'}",
        f"**Selected products (build order):** {', '.join(f'`{product}`' for product in selected) or 'None'}",
        "",
    ]
    if paths:
        lines.extend(["### Dependency impact paths", ""])
        for product, chains in sorted(paths.items()):
            lines.append(f"- **{product}:** " + "; ".join(f"`{chain}`" for chain in chains))
        lines.append("")

    for scenario, title in (
        ("full", "Full-build dependency graph"),
        ("changed", "Changed-products dependency graph"),
    ):
        lines.extend([f"### {title}", "", "```mermaid", graphs[scenario], "```", ""])

    if artifact_url:
        parsed_url = urlparse(artifact_url)
        if parsed_url.scheme in {"http", "https"} and parsed_url.netloc:
            lines.extend([f"[Download the complete dependency report]({artifact_url})", ""])
    return "\n".join(lines)


def render_html(report: dict, graphs: dict[str, str]) -> str:
    graph_sections = "\n".join(
        f'<section><h2>{title}</h2><pre class="mermaid">{html.escape(graph)}</pre></section>'
        for scenario, title in (
            ("full", "Full-build dependency graph"),
            ("changed", "Changed-products dependency graph"),
        )
        for graph in (graphs[scenario],)
    )
    changed = ", ".join(report.get("changedProducts", [])) or "None"
    selected = ", ".join(report.get("selectedProducts", [])) or "None"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pipeline dependency graphs</title>
  <style>
    body {{ font: 16px system-ui, sans-serif; margin: 2rem auto; max-width: 90rem; padding: 0 1rem; }}
    .mermaid {{ overflow-x: auto; }}
  </style>
  <script type="module">
    import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
    mermaid.initialize({{ startOnLoad: true, securityLevel: "strict" }});
  </script>
</head>
<body>
  <h1>Pipeline dependency graphs</h1>
  <p><strong>Build scenario:</strong> {html.escape(str(report["mode"]))}</p>
  <p><strong>Changed products:</strong> {html.escape(changed)}</p>
  <p><strong>Selected products (build order):</strong> {html.escape(selected)}</p>
  {graph_sections}
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, help="Write a standalone HTML graph report.")
    parser.add_argument("--mermaid-dir", type=Path, default=DEFAULT_REPORT_DIR)
    parser.add_argument("--summary", type=Path, help="Append Markdown to a GitHub Actions step summary.")
    parser.add_argument("--artifact-url", help="Link to the uploaded dependency-report artifact.")
    args = parser.parse_args()
    if not args.html and not args.summary:
        parser.error("at least one of --html or --summary is required")

    report_dir = args.mermaid_dir
    try:
        report, graphs = read_report(report_dir)
        if args.html:
            args.html.parent.mkdir(parents=True, exist_ok=True)
            args.html.write_text(render_html(report, graphs), encoding="utf-8")
        if args.summary:
            args.summary.parent.mkdir(parents=True, exist_ok=True)
            with args.summary.open("a", encoding="utf-8") as summary_file:
                summary_file.write(render_markdown(report, graphs, args.artifact_url))
    except (OSError, json.JSONDecodeError, KeyError) as error:
        print(f"Could not render dependency summary: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
