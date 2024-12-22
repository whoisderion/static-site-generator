import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    # def test_no_tag(self):
    # node =

    # def test_no_children(self):

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


if __name__ == "__main__":
    unittest.main()
