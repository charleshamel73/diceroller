from src.constant.Number import Number
from src.operator.Operator import Operator
from src.result.Result import Result
from src.roll.Diceroll import Diceroll
from src.visitor.NodeVisitor import NodeVisitor


class ResultVisitor(NodeVisitor):
    @classmethod
    def visit(cls,node):
        if isinstance(node,Diceroll):
            rolls = node.rollDice()
            return Result(node.get_sum_of_roll(),rolls)
        if isinstance(node, Operator):
            resultLeft = node.left
            resultRight = node.right
            return resultLeft.merge_results(resultRight,node)
        if isinstance(node,Number):
            return Result(node.getValue())
        else:
            raise TypeError("TYPE ERROR: Result Visitor has found a type it can not handle. Found %s"%node.__class__)