from src.parser.Operator import Operator

class Subtraction(Operator):
    symbol = "-"
    def evaluate(self):
        return self.leftChild.evaluate() - self.rightChild.evaluate()