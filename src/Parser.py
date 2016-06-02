class Parser(object):
    def parse(self,string):
        from NodeFactory import NodeFactory
        root = NodeFactory.fetch_part(string)
        return root.evaluate()