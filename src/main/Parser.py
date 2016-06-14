from src.visitor.LogResultVisitor import ResultVisitor
from src.visitor.SyntaxCheckVisitor import SyntaxVisitor
from src.visitor.ValueCheckVisitor import ValueCheckVisitor


class Parser(object):
    def parse(self,string):
        from NodeFactory import NodeFactory
        #BEFORE COMPILE
        root = NodeFactory.fetch_part(string)
        root.accept(SyntaxVisitor)
        #COMPILE
        #TODO: CREATE EVALUATE STEP
        #AFTER COMPILE
        root.accept(ValueCheckVisitor)
        #TODO: RENAME RESULTVISITOR
        test = root.accept(ResultVisitor)
        return test.sum