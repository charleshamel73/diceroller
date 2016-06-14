from src.visitor.CompileVisitor import CompileVisitor
from src.visitor.LogResultVisitor import LogResultVisitor
from src.visitor.SyntaxCheckVisitor import SyntaxVisitor
from src.visitor.ValueCheckVisitor import ValueCheckVisitor


class Parser(object):
    def parse(self,string):
        from NodeFactory import NodeFactory
        #BEFORE COMPILE
        root = NodeFactory.fetch_part(string)
        root.accept(SyntaxVisitor)
        #COMPILE
        root.accept(CompileVisitor)
        root.accept(ValueCheckVisitor)
        #AFTER COMPILE
        test = root.accept(LogResultVisitor)
        return test.sum