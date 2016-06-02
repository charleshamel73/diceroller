from Node import Node


class Number(Node):
    def __init__(self, string):
        if string == "":
            raise ValueError("Number Error: Found empty string when parsing Number")
        if "-" in string:
            raise ValueError("Number Error: Number can not be negative")

        self.string = string

    def evaluate(self):
        return int(self.string)
