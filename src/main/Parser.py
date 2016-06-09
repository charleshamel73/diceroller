class Parser(object):
    def parse(self,string):
        from NodeFactory import NodeFactory
        root = NodeFactory.fetch_part(string)
        root.validate()
        return root.evaluate()
