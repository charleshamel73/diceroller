from src.visitor.CompileVisitor import CompileVisitor
from src.visitor.LogResultVisitor import LogResultVisitor
from src.visitor.SyntaxCheckVisitor import SyntaxVisitor
from src.visitor.ValueCheckVisitor import ValueCheckVisitor


class Parser(object):
    def parse(self,string):
        from NodeFactory import NodeFactory
        print "ROLL '%s'"%string
        print "PARSING STRING"
        root = NodeFactory.fetch_part(string)
        print "CHECKING SYNTAX"
        root.accept(SyntaxVisitor)
        print "COMPILING"
        root.accept(CompileVisitor)
        print "CHECKING VALUES"
        root.accept(ValueCheckVisitor)
        print "LOGGING RESULTS"
        test = root.accept(LogResultVisitor)
        print "Result of Roll: %s"%test.sum
        print ""
        return test