from src.constant.Number import Number
from src.modifier.Highest import Highest
from src.modifier.Lowest import Lowest
from src.operator.Addition import Addition
from src.operator.Divide import Divide
from src.operator.Multiply import Multiply
from src.operator.Subtraction import Subtraction
from src.roll.Diceroll import Diceroll
from src.roll import Keep
from src.roll import Reroll


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
        # elif Keep.symbol in string:
        #     return Keep(string)
        # elif Reroll.symbol in string:
        #     return Reroll(string)
        elif Diceroll.symbol in string:
            return Diceroll(string)
        elif Highest.symbol in string:
            return Highest(string)
        elif Lowest.symbol in string:
            return Lowest(string)
        elif string != "":
            return Number(string)
        else:
            raise SyntaxError("PARSING ERROR: Found empty string when parsing. Roll contains a negative number")