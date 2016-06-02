from src.parser.Operator import Operator

class Multiply(Operator):
    symbol = "*"
    def evaluate(self):
        return self.leftChild.evaluate() * self.rightChild.evaluate()