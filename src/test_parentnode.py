import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "BOLD"),
                LeafNode(None, "NORMAL"),
                LeafNode("i", "ITALIC"),
                LeafNode(None, "NORMAL"),
            ],
        )
        self.assertRaises(ValueError, node.to_html)

    def test_no_children(self):
        node = ParentNode("p", [])
        self.assertRaises(ValueError, node.to_html)

    def test_4_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "BOLD"),
                LeafNode(None, "NORMAL"),
                LeafNode("i", "ITALIC"),
                LeafNode(None, "NORMAL"),
            ],
        )

        node.to_html()

    def test_nested_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "BOLD"),
                LeafNode(None, "NORMAL"),
                ParentNode("i", [LeafNode("b", "italibold")]),
                LeafNode(None, "NORMAL"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>BOLD</b>NORMAL<i><b>italibold</b></i>NORMAL</p>",
        )

    def test_props(self):
        node = ParentNode(
            "a",
            [LeafNode("p", "click me!", {"prop": "swag"})],
            {"href": "https://www.google.com"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com"><p prop="swag">click me!</p></a>',
        )


if __name__ == "__main__":
    unittest.main()
