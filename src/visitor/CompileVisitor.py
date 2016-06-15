from src.constant.Number import Number
from src.modifier.Modifier import Modifier
from src.operator.Operator import Operator
from src.roll.Roll import Roll
from src.visitor.NodeVisitor import NodeVisitor


class CompileVisitor(NodeVisitor):
    @classmethod
    def visit(cls,node):
        if isinstance(node, Roll):
            node.dice_roll()
        elif isinstance(node,Number):
            node.value = int(node.string)
        elif isinstance(node,(Operator, Modifier)):
            print("COMPILE INFO: No Compile needed for %s Node" % node.__class__.__name__)
        else:
            raise TypeError("TYPE ERROR: Result Visitor has found a type it can not handle. Found %s"%node.__class__)