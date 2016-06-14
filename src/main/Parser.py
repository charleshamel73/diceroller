from src.visitor.ResultVisitor import ResultVisitor
from src.visitor.SyntaxVisitor import SyntaxVisitor


class Parser(object):
    def parse(self,string):
        from NodeFactory import NodeFactory
        root = NodeFactory.fetch_part(string)
        root.accept(SyntaxVisitor)
        test = root.accept(ResultVisitor)
        return test.sum