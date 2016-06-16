from src.main.Node import Node


class Modifier(Node):
    child = None
    childNode = None

    def __init__(self, string):
        from src.main.NodeFactory import NodeFactory
        self.string = string
        string_without_sym = string.replace(self.symbol, "")
        self.child = NodeFactory.fetch_part(string_without_sym)

    def accept(self, visitor):
        self.childNode = self.child.accept(visitor)
        return visitor.visit(self)

    def getValue(self):
        return self.child.getValue()
