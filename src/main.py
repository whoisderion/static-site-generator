from textnode import TextNode, TextType


def main():
    test_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test_node)


main()
