from src.constant.Number import Number
from src.modifier.Modifier import Modifier
from src.operator.Operator import Operator
from src.result.Result import Result
from src.roll.Roll import Roll
from src.visitor.NodeVisitor import NodeVisitor


class LogResultVisitor(NodeVisitor):
    @classmethod
    def visit(cls,node):
        if isinstance(node, Roll):
            return Result(node.get_sum_of_roll(), node.rolls)
        elif isinstance(node, Operator):
            resultLeft = node.left
            resultRight = node.right
            return resultLeft.merge_results(resultRight, node)
        elif isinstance(node,Number):
            return Result(node.getValue())
        elif isinstance(node, Modifier):
            print("LOG RESULT INFO: No Result to get from %s Node" % node.__class__.__name__)
        else:
            raise TypeError("TYPE ERROR: Result Visitor has found a type it can not handle. Found %s"%node.__class__)