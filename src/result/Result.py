class Result(object):
    sum = 0
    rolls = []

    def __init__(self, sum, roll=None):
        self.sum = sum
        if roll is not None:
            self.rolls = roll

    def merge_results(self, result, type):
        from src.operator.Multiply import Multiply
        from src.operator.Addition import Addition
        from src.operator.Divide import Divide
        from src.operator.Subtraction import Subtraction
        if isinstance(type, Addition):
            self.sum += result.sum
        elif isinstance(type, Subtraction):
            self.sum -= result.sum
        elif isinstance(type, Multiply):
            self.sum *= result.sum
        elif isinstance(type, Divide):
            self.sum /= result.sum
        else:
            raise TypeError("TYPE ERROR: Results can only be of type Operator. Found Type %s" % type.__class__)
        return self
