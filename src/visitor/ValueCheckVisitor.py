from src.constant.Number import Number
from src.modifier.Modifier import Modifier
from src.operator.Operator import Operator
from src.roll.Diceroll import Diceroll
from src.roll.Keep import Keep
from src.roll.Reroll import Reroll
from src.visitor.NodeVisitor import NodeVisitor


class ValueCheckVisitor(NodeVisitor):
    @classmethod
    def visit(cls, node):
        if isinstance(node, Reroll):
            if node.reroll > node.numberOfSides:
                raise ValueError(
                    "REROLL VALUE ERROR: Expected a Reroll Number less then the number of sides but found '%s'" % node.numberOfSides)
        if isinstance(node, Keep):
            if node.keep_count > node.numberOfSides:
                raise ValueError("REROLL VALUE ERROR: Expected a Keep Count less then the number of dice rolled but found '%s'" % node.numberOfSides)
        elif isinstance(node, Number):
            if node.getValue() <= 0:
                raise ValueError("NUMBER VALUE ERROR: Expected number greater then 0 got '%s'" % node.getValue())
        elif isinstance(node,(Diceroll,Operator,Modifier)):
            print("VALUE CHECK INFO: No Value Check needed for %s Node" % node.__class__.__name__)
        else:
            raise TypeError("TYPE ERROR: ValueCheckVisitor has found a type it can not handle. Found %s" % node.__class__)
