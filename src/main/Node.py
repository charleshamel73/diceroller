class Node(object):
    string = ""
    symbol = ""

    def evaluate(self):
        raise Exception("Error: Node must implement evaluate()")

    def validate(self):
        raise Exception("Error: Node must implement validate()")