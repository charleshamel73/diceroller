from src.constant.Number import Number
from src.operator.Operator import Operator
from src.result.Result import Result
from src.roll.Diceroll import Diceroll
from src.visitor.NodeVisitor import NodeVisitor


class CompileVisitor(NodeVisitor):
    @classmethod
    def visit(cls,node):
        if isinstance(node,Diceroll):
            pass
            #node.rollDice()
            #node.
            #return Result(node.get_sum_of_roll(),rolls)
        elif isinstance(node,Number):
            node.value = int(node.string)
        elif isinstance(node,Operator):
            pass
        else:
            raise TypeError("TYPE ERROR: Result Visitor has found a type it can not handle. Found %s"%node.__class__)