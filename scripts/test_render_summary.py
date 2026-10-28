import tempfile
import unittest
from pathlib import Path

from render_summary import read_report, render_html, render_markdown


class RenderSummaryTest(unittest.TestCase):
    def setUp(self):
        self.report = {
            "mode": "changed",
            "changedProducts": ["catalog"],
            "selectedProducts": ["thirdparty", "catalog"],
            "dependencyPaths": {"catalog": ["catalog -> orders"]},
        }
        self.graphs = {
            "full": "flowchart LR\n  full --> graph",
            "changed": "flowchart LR\n  catalog --> orders",
        }

    def test_summary_contains_both_inline_graphs_and_impact_paths(self):
        summary = render_markdown(
            self.report,
            self.graphs,
            "https://github.com/actions/runs/123/artifacts/456",
        )

        self.assertIn("### Full-build dependency graph", summary)
        self.assertIn("### Changed-products dependency graph", summary)
        self.assertEqual(summary.count("```mermaid"), 2)
        self.assertIn("`catalog -> orders`", summary)
        self.assertIn("[Download the complete dependency report]", summary)

    def test_summary_ignores_non_http_artifact_urls(self):
        summary = render_markdown(self.report, self.graphs, "javascript:alert(1)")

        self.assertNotIn("Download the complete dependency report", summary)

    def test_html_contains_renderable_graphs_and_escapes_graph_markup(self):
        html_report = render_html(
            self.report,
            {
                "full": 'flowchart LR\n  node["<script>"]',
                "changed": self.graphs["changed"],
            },
        )

        self.assertEqual(html_report.count('class="mermaid"'), 2)
        self.assertIn("&lt;script&gt;", html_report)
        self.assertNotIn('<pre class="mermaid">flowchart LR\n  node["<script>"]', html_report)

    def test_read_report_loads_json_and_both_graph_files(self):
        with tempfile.TemporaryDirectory() as directory:
            report_dir = Path(directory)
            (report_dir / "dependency-graph.json").write_text(
                '{"mode":"full"}', encoding="utf-8"
            )
            for scenario in ("full", "changed"):
                (report_dir / f"dependency-graph-{scenario}.mmd").write_text(
                    f"flowchart LR\n  {scenario}", encoding="utf-8"
                )

            report, graphs = read_report(report_dir)

        self.assertEqual(report["mode"], "full")
        self.assertEqual(graphs["full"], "flowchart LR\n  full")
        self.assertEqual(graphs["changed"], "flowchart LR\n  changed")


if __name__ == "__main__":
    unittest.main()
