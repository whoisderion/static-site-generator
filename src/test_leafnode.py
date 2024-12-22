import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf_node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_link(self):
        leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            leaf_node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_empty(self):
        leaf_node = LeafNode(None, "I'm so hollow")
        self.assertEqual(
            leaf_node.to_html(),
            "I'm so hollow",
        )


if __name__ == "__main__":
    unittest.main()
