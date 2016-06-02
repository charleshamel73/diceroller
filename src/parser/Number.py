from src.parser.Operator import Operator


class Number(Operator):
    def __init__(self, string):
        self.string = string

    def evaluate(self):
        return int(self.string)
