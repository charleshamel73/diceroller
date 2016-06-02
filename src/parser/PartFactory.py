from src.parser.Addition import Addition
from src.parser.Divide import Divide
from src.parser.Highest import Highest
from src.parser.Lowest import Lowest
from src.parser.Multiply import Multiply
from src.parser.Number import Number
from src.parser.Roll import Roll
from src.parser.Subtraction import Subtraction


class PartFactory:
    def __init__(self):
        pass

    @classmethod
    def fetch_part(cls, string):
        if Subtraction.symbol in string:
            return Subtraction(string)
        elif Addition.symbol in string:
            return Addition(string)
        elif (Divide.symbol in string):
            return Divide(string)
        elif (Multiply.symbol in string):
            return Multiply(string)
        elif(Roll.symbol in string):
            return Roll(string)
        elif Highest.symbol in string:
            return Highest(string)
        elif Lowest.symbol in string:
            return Lowest(string)
        else:
            return Number(string)