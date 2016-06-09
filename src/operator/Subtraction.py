from src.constant.Number import Number
from src.operator.Keep import Keep
from src.operator.Operator import Operator
from src.operator.Reroll import Reroll
from src.operator.Roll import Roll


class Subtraction(Operator):
    symbol = "-"

    def evaluate(self):
        return self.leftChild.evaluate() - self.rightChild.evaluate()

    def validate(self):
        self.leftChild.validate()
        self.rightChild.validate()
        if not isinstance(self.leftChild, (Roll, Reroll, Keep, Number)):
            raise SyntaxError("SUBTRACTION SYNTAX ERROR: Expected Roll or Number to the left but got '%s'"%self.leftChild.string)
        if not isinstance(self.leftChild, (Roll, Reroll, Keep, Number)):
            raise SyntaxError("SUBTRACTION SYNTAX ERROR: Expected Roll or Number to the left but got '%s'"%self.rightChild.string)