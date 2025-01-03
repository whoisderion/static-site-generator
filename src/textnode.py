from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold-text"
    ITALIC = "italic-text"
    CODE = "code-text"
    LINK = "link-text"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_text):
        if (
            self.text == other_text.text
            and self.text_type == other_text.text_type
            and self.url == other_text.url
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f'TextNode("{self.text}", {self.text_type.value}, {self.url})'


def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    if text_type == None:
        raise Exception("TextNode must have a text type!")
    elif text_type not in TextType:
        raise Exception("TextNode must have a valid text type!")

    if text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
