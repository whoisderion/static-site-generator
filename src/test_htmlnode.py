import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_p(self):
        htmlnode = HTMLNode("p", "this is a paragraph!")

        self.assertEqual(
            repr(htmlnode),
            "Tag: p\nValue: this is a paragraph!\nChildren: None\nProps: None",
        )

    def test_a(self):
        htmlnode = HTMLNode("a", "boot.dev")
        self.assertEqual(
            repr(htmlnode),
            "Tag: a\nValue: boot.dev\nChildren: None\nProps: None",
        )

    def test_empty(self):
        htmlnode = HTMLNode("p", "")
        self.assertEqual(
            repr(htmlnode),
            "Tag: p\nValue: \nChildren: None\nProps: None",
        )


if __name__ == "__main__":
    unittest.main()
