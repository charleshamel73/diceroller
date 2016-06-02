from Divide import Divide
from Highest import Highest
from Lowest import Lowest
from Multiply import Multiply
from Number import Number
from Subtraction import Subtraction
from Addition import Addition
from Roll import Roll


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
        elif Roll.symbol in string:
            return Roll(string)
        elif Highest.symbol in string:
            return Highest(string)
        elif Lowest.symbol in string:
            return Lowest(string)
        else:
            return Number(string)

    @classmethod
    def fetch_value(cls,string):
        if Highest.symbol in string:
            return Highest(string)
        elif Lowest.symbol in string:
            return Lowest(string)
        else:
            return Number(string)