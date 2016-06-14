class NodeVisitor:
    def __init__(self):
        pass

    @classmethod
    def visit(cls,node):
        raise Exception("Must implement visit function if inheriting NodeVisitor")