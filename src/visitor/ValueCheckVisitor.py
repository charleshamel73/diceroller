from src.constant.Number import Number
from src.operator.Operator import Operator
from src.roll.Diceroll import Diceroll
from src.roll.Keep import Keep
from src.roll.Reroll import Reroll
from src.visitor.NodeVisitor import NodeVisitor


class ValueCheckVisitor(NodeVisitor):
    @classmethod
    def visit(cls, node):
        if isinstance(node, Number):
            if node.getValue() <= 0:
                raise ValueError("NUMBER VALUE ERROR: Expected number greater then 0 got '%s'" % node.getValue())
        elif isinstance(node,(Diceroll,Operator)):
            pass
        else:
            raise TypeError("TYPE ERROR: ValueCheckVisitor has found a type it can not handle. Found %s" % node.__class__)

