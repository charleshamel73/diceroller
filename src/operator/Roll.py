import random

from src.constant.Number import Number
from src.operator.Operator import Operator


class Roll(Operator):
    symbol = "d"
    numberOfDice = None
    numberOfSides = None
    rolls = []

    def evaluate(self):
        self.numberOfDice = self.leftChild.evaluate()
        self.numberOfSides = self.rightChild.evaluate()
        self.rolls = []
        sum = 0
        for i in range(0, self.numberOfDice):
            roll = random.randint(1, self.numberOfSides)
            self.rolls.append(roll)
            sum += roll
        #Return roll to be digested by the above class in case of another operator consuming it
        print "ROLL: rolls for '%s': %s with a sum of %s" % (self.string, self.rolls, sum)
        return sum

    def validate(self):
        self.leftChild.validate()
        self.rightChild.validate()
        if not isinstance(self.leftChild,Number):
            raise SyntaxError("ROLL SYNTAX ERROR: Expected number on left side of roll. Got '%s'"%self.leftChild.string)
        if not isinstance(self.rightChild,Number):
            raise SyntaxError("ROLL SYNTAX ERROR: Expected number on right side of roll. Got '%s'"%self.rightChild.string)
