from src.parser.Operator import Operator

class Divide(Operator):
    symbol = "/"
    def evaluate(self):
        return self.leftChild.evaluate() / self.rightChild.evaluate()