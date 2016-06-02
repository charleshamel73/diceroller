from Node import Node


class Subtraction(Node):
    symbol = "-"

    def evaluate(self):
        return self.leftChild.evaluate() - self.rightChild.evaluate()
