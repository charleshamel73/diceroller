from src.constant.Number import Number
from src.operator.Operator import Operator
from src.roll.Diceroll import Diceroll
from src.roll.Keep import Keep
from src.roll.Reroll import Reroll
from src.visitor.NodeVisitor import NodeVisitor


class SyntaxVisitor(NodeVisitor):
    @classmethod
    def visit(cls, node):
        if isinstance(node, Diceroll):
            if not isinstance(node.leftChild, Number):
                raise SyntaxError(
                    "ROLL SYNTAX ERROR: Expected number on left side of roll. Got '%s'" % node.leftChild.string)
            if not isinstance(node.rightChild, Number):
                raise SyntaxError(
                    "ROLL SYNTAX ERROR: Expected number on right side of roll. Got '%s'" % node.rightChild.string)
        if isinstance(node, Operator):
            if not isinstance(node.leftChild, (Diceroll, Reroll, Keep, Number)):
                raise SyntaxError(
                    "OPERATOR SYNTAX ERROR: Expected Roll or Number to the left but got '%s'" % node.leftChild.string)
            if not isinstance(node.leftChild, (Diceroll, Reroll, Keep, Number)):
                raise SyntaxError(
                    "OPERATOR SYNTAX ERROR: Expected Roll or Number to the left but got '%s'" % node.rightChild.string)
        elif isinstance(node, Number):
            try:
                node.getValue()
            except ValueError:
                raise SyntaxError("NUMBER SYNTAX ERROR: Expected number without characters but got '%s'" % node.getValue())
        else:
            raise TypeError("TYPE ERROR: Result Visitor has found a type it can not handle. Found %s" % node.__class__)

