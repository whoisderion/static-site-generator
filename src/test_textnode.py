import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_url_none_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_type_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Me too!", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_convert_normal(self):
        tn = TextNode("This is text node", TextType.TEXT)
        tn = text_node_to_html_node(tn)
        self.assertEqual(tn.to_html(), "This is text node")

    def test_convert_bold(self):
        tn = TextNode("This is a bolded node", TextType.BOLD)
        tn = text_node_to_html_node(tn)
        self.assertEqual(tn.to_html(), "<b>This is a bolded node</b>")

    def test_convert_italic(self):
        tn = TextNode("This is an italicized node", TextType.ITALIC)
        tn = text_node_to_html_node(tn)
        self.assertEqual(tn.to_html(), "<i>This is an italicized node</i>")

    def test_convert_code(self):
        tn = TextNode("Hello world", TextType.CODE)
        tn = text_node_to_html_node(tn)
        self.assertEqual(tn.to_html(), "<code>Hello world</code>")

    def test_convert_link(self):
        tn = TextNode("Surfing the web!", TextType.LINK, "https://google.com")
        tn = text_node_to_html_node(tn)
        self.assertEqual(
            tn.to_html(), '<a href="https://google.com">Surfing the web!</a>'
        )

    def test_convert_image(self):
        tn = TextNode(
            "Monke",
            TextType.IMAGE,
            "https://i.kym-cdn.com/photos/images/original/001/867/654/334.jpg",
        )
        tn = text_node_to_html_node(tn)
        self.assertEqual(
            tn.to_html(),
            '<img src="https://i.kym-cdn.com/photos/images/original/001/867/654/334.jpg" alt="Monke"></img>',
        )

    def test_convert_no_text_type(self):
        with self.assertRaises(Exception):
            tn = TextNode("I don't have a type", None)
            tn = text_node_to_html_node(tn)

    def test_convert_image_no_text(self):
        tn = TextNode(
            None,
            TextType.IMAGE,
            "https://i.kym-cdn.com/photos/images/original/001/867/654/334.jpg",
        )
        tn = text_node_to_html_node(tn)
        self.assertEqual(
            tn.to_html(),
            '<img src="https://i.kym-cdn.com/photos/images/original/001/867/654/334.jpg" alt="None"></img>',
        )

    def test_convert_link_no_link(self):
        tn = TextNode("Surfing the web!", TextType.LINK)
        tn = text_node_to_html_node(tn)
        self.assertEqual(tn.to_html(), '<a href="None">Surfing the web!</a>')


if __name__ == "__main__":
    unittest.main()
