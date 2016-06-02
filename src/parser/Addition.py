from src.parser.Operator import Operator

class Addition(Operator):
    symbol = "+"
    def evaluate(self):
        return self.leftChild.evaluate() + self.rightChild.evaluate()