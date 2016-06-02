class Node(object):
    parent = None
    leftChild = None
    rightChild = None
    symbol = ""
    string = ""

    def __init__(self, string):
        from NodeFactory import NodeFactory
        self.string = string
        parts = string.split(self.symbol, 1)
        self.leftChild = NodeFactory.fetch_part(parts[0])
        self.rightChild = NodeFactory.fetch_part(parts[1])

    def evaluate(self):
        raise Exception("Error: Node must implement evaluate()")
