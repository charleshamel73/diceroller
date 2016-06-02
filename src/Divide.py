from Node import Node


class Divide(Node):
    symbol = "/"

    def evaluate(self):
        return self.leftChild.evaluate() / self.rightChild.evaluate()
