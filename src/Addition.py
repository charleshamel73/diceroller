from Node import Node


class Addition(Node):
    symbol = "+"

    def evaluate(self):
        return self.leftChild.evaluate() + self.rightChild.evaluate()
