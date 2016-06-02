from Node import Node


class Multiply(Node):
    symbol = "*"

    def evaluate(self):
        return self.leftChild.evaluate() * self.rightChild.evaluate()
