class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self._tag = tag
        self._value = value
        self._children = children
        self._props = props

    def __repr__(self):
        props_list = self.props_to_html()
        node = f"Tag: {self._tag}\nValue: {self._value}\nChildren: {self._children}\nProps: {props_list}"
        return node

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_list = ""
        if self._props != None:
            for prop in self._props:
                props_list += f' {prop}="{self._props[prop]}"'
        else:
            props_list += "None"
        return props_list

    def get_children(self):
        return self._children

    def get_props(self):
        return self._props


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self._value == None:
            raise ValueError
        if self._tag == None:
            return self._value
        if self._props == None:
            return f"<{self._tag}>{self._value}</{self._tag}>"
        return f"<{self._tag}{self.props_to_html()}>{self._value}</{self._tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self._tag == None:
            raise ValueError("Parent nodes must have a tag")
        elif self._children == None or self._children == []:
            raise ValueError("Parent nodes must have children")
        elif self._props == None:
            return f"<{self._tag}>{self.print_children(self._children)}</{self._tag}>"
        return f"<{self._tag}{self.props_to_html()}>{self.print_children(self._children)}</{self._tag}>"

    def print_children(self, children, children_str=""):
        if len(children) < 1:
            return ""

        next_child = children[0]

        if next_child.get_children() == None:
            return (
                children_str
                + next_child.to_html()
                + self.print_children(children[1:], children_str)
            )

        return (
            children_str
            + next_child.to_html()
            + self.print_children(children[1:], children_str)
        )
