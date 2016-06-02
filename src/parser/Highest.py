from src.parser.Operator import Operator

class Highest(Operator):
    symbol = "H"
    def __init__(self, string):
        self.string = string

    def evaluate(self):
        return int(self.string.replace(self.symbol,""))