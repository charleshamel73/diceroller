from src.main.Node import Node


class Modifier(Node):
    child = None

    def __init__(self, string):
        from src.main.NodeFactory import NodeFactory
        self.string = string
        string_without_sym = string.replace(self.symbol, "")
        self.child = NodeFactory.fetch_part(string_without_sym)
