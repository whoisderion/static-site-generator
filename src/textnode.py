from enum import Enum


class TextType(Enum):
    NORMAL = "normal-text"
    BOLD = "bold-text"
    ITALIC = "italic-text"
    CODE = "code-text"
    LINK = "link-text"
    IMAGES = "image"


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
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
