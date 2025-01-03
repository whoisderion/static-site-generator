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


if __name__ == "__main__":
    unittest.main()
