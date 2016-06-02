from Node import Node
from src.Number import Number


class Highest(Node):
    symbol = "H"

    def __init__(self, string):
        string.replace(self.symbol, "")
        self.number = Number(string)

    def evaluate(self):
        return self.number.evaluate()