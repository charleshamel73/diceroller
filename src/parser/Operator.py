from src.parser.PartFactory import PartFactory


class Operator:
    parent = None
    leftChild = None
    rightChild = None
    symbol = ""
    string = ""

    def __init__(self, string):
        self.string = string
        parts = string.split(self.symbol,1)
        self.leftChild = PartFactory.fetch_part(parts[0])
        self.rightChild = PartFactory.fetch_part(parts[1])

    def evaluate(self):
        raise Exception("Error: Node must implement evaluate()")