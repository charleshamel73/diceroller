from src.main.Node import Node


class Operator(Node):
    leftChild = None
    rightChild = None
    left = None
    right = None

    def __init__(self, string):
        from src.main.NodeFactory import NodeFactory
        self.string = string
        parts = string.split(self.symbol, 1)
        self.leftChild = NodeFactory.fetch_part(parts[0])
        self.rightChild = NodeFactory.fetch_part(parts[1])

    def accept(self, visitor):
        self.left = self.leftChild.accept(visitor)
        self.right = self.rightChild.accept(visitor)
        return visitor.visit(self)
