class Result(object):
    sum = 0
    rolls = []
    message = ""

    def __init__(self, sum, roll=None,message=None):
        self.sum = sum
        if roll is not None:
            self.rolls = roll
        if message is not None:
            self.message = message

    def merge_results(self, result, type,operator_message):
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
        self.message += result.message
        self.message += operator_message
        return self

    #TODO: Create merge roll

    #TODO: Create set message??

    #TODO: merge message?
