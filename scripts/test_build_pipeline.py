import unittest

from build_pipeline import discover_graph, select_products


class BuildPipelineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.products, cls.graph, cls.maven_edges, cls.osgi_edges = discover_graph()

    def test_changed_product_includes_dependents_and_prerequisites(self):
        changed, selected, paths = select_products(
            self.products,
            "changed",
            ["osgi-workshop/customer/plugins/com.northwind.oms.customer/src/Customer.java"],
            self.graph["productDependencies"],
        )

        self.assertEqual(changed, ["customer"])
        self.assertEqual(
            selected,
            ["thirdparty", "catalog", "customer", "shipping", "notification"],
        )
        self.assertIn("customer -> shipping", paths["customer"])
        self.assertIn("customer -> shipping -> notification", paths["customer"])

    def test_manifest_package_dependency_is_in_osgi_graph(self):
        self.assertTrue(
            any(
                edge["from"] == "com.northwind.oms.gateway"
                and edge["to"] == "com.northwind.oms.core"
                and edge["kind"] == "imports-package"
                for edge in self.osgi_edges
            )
        )

    def test_feature_dependency_is_in_product_graph(self):
        self.assertIn("catalog", self.graph["productDependencies"]["orders"])

    def test_root_build_configuration_change_selects_every_product(self):
        changed, selected, _ = select_products(
            self.products,
            "changed",
            ["osgi-workshop/pom.xml"],
            self.graph["productDependencies"],
        )

        self.assertEqual(changed, self.products)
        self.assertEqual(set(selected), set(self.products))


if __name__ == "__main__":
    unittest.main()
