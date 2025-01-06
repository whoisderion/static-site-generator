import re

from textnode import TextNode


def split_nodes(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        sections = old_node.text.split(delimiter)
        for index, split_node in enumerate(sections):
            if split_node == "":
                continue
            if index % 2 == 0:
                new_nodes.append(TextNode(split_node, old_node.text_type))
            else:
                new_nodes.append(TextNode(split_node, text_type))
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
