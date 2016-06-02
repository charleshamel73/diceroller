from src.parser.Operator import Operator

class Lowest(Operator):
    symbol = "L"
    def __init__(self, string):
        self.string = string

    def evaluate(self):
        return int(self.string.replace(self.symbol,""))