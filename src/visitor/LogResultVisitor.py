from src.constant.Number import Number
from src.modifier.Modifier import Modifier
from src.operator.Addition import Addition
from src.operator.Divide import Divide
from src.operator.Multiply import Multiply
from src.operator.Operator import Operator
from src.operator.Subtraction import Subtraction
from src.result.Result import Result
from src.roll.Diceroll import Diceroll
from src.roll.Keep import Keep
from src.roll.Reroll import Reroll
from src.roll.Roll import Roll
from src.visitor.NodeVisitor import NodeVisitor


class LogResultVisitor(NodeVisitor):
    @classmethod
    def visit(cls,node):
        if isinstance(node,Roll):
            #TODO: Roll -> Keep overwrites message in result
            #TODO: if message != "" add message instead of delete maybe??
            if isinstance(node, Reroll):
                status = ("Rerolled all %s and got %s with a sum of %s"
                       % (node.reroll, node.rolls, node.get_sum_of_roll()))
            elif isinstance(node, Keep):
                status = ("Kept %s %s values and got %s with a sum of %s"
                   % (node.keep_count, node.rightChild.__class__.__name__,node.rolls, node.get_sum_of_roll()))
            elif isinstance(node, Diceroll):
                status = ("Rolled '%s' and got %s with a sum of %s"%(node.string,node.rolls,node.get_sum_of_roll()))
            return Result(node.get_sum_of_roll(), node.rolls,status)
        elif isinstance(node, Operator):
            resultLeft = node.left
            resultRight = node.right
            verb = ""
            if isinstance(node,Addition):
                verb = "Adding"
            elif isinstance(node,Subtraction):
                verb = "Subtracting"
            elif isinstance(node,Multiply):
                verb = "Multipling"
            elif isinstance(node,Divide):
                verb = "Dividing"
            if isinstance(node.rightChild,Number):
                status = "%s by %s to get a total value of %s"\
                      %(verb, node.rightChild.getValue(), resultLeft.sum)
            elif isinstance(node.rightChild,Roll):
                status = "%s previous total by new roll to get %s" \
                      % (verb, node.left.sum)
            resultLeft.merge_results(resultRight, node,status)
            return resultLeft
        elif isinstance(node,Number):
            #TODO: IF I TRACK PARENT I CAN OUTPUT STARTING AT ??
            return Result(node.getValue())
        elif isinstance(node, Modifier):
            print("LOG RESULT INFO: No Result to get from %s Node" % node.__class__.__name__)
        else:
            raise TypeError("TYPE ERROR: Result Visitor has found a type it can not handle. Found %s"%node.__class__)