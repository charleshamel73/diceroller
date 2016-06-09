from src.constant.Number import Number
from src.modifier.Highest import Highest
from src.modifier.Lowest import Lowest
from src.operator.Reroll import Reroll
from src.operator.Addition import Addition
from src.operator.Divide import Divide
from src.operator.Keep import Keep
from src.operator.Multiply import Multiply
from src.operator.Roll import Roll
from src.operator.Subtraction import Subtraction


class NodeFactory(object):
    def __init__(self):
        pass

    @classmethod
    def fetch_part(cls, string):
        if Subtraction.symbol in string:
            return Subtraction(string)
        elif Addition.symbol in string:
            return Addition(string)
        elif Divide.symbol in string:
            return Divide(string)
        elif Multiply.symbol in string:
            return Multiply(string)
        elif Keep.symbol in string:
            return Keep(string)
        elif Reroll.symbol in string:
            return Reroll(string)
        elif Roll.symbol in string:
            return Roll(string)
        elif Highest.symbol in string:
            return Highest(string)
        elif Lowest.symbol in string:
            return Lowest(string)
        elif string != "":
            return Number(string)
        else:
            raise SyntaxError("PARSING ERROR: Found empty string when parsing. Roll contains a negative number")