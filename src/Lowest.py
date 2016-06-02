from Node import Node
from src.Number import Number


class Lowest(Node):
    symbol = "L"
    number = None

    def __init__(self, string):
        string.replace(self.symbol, "")
        self.number = Number(string)

    def evaluate(self):
        return self.number.evaluate()
