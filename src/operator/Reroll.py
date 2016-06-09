import random

from src.constant.Number import Number
from src.operator.Roll import Roll
from src.operator.Operator import Operator


class Reroll(Operator):
    symbol = "r"
    rolls = []
    numberOfSides = None

    def evaluate(self):
        dice_roll = self.leftChild
        self.numberOfSides = dice_roll.numberOfSides
        reroll = self.rightChild.evaluate()
        self.rolls = []
        sum = 0
        for roll in dice_roll.rolls:
            while roll == reroll:
                roll = random.randint(1, dice_roll.sides)
            self.rolls.append(roll)
            sum += roll
        # Always return the result of the roll
        print "REROLL: rolls for '%s': %s with a sum of %s" % (self.string, self.rolls, sum)
        return sum

    def validate(self):
        self.leftChild.validate()
        self.rightChild.validate()
        if not isinstance(self.leftChild, Roll):
            raise SyntaxError("REROLL SYNTAX ERROR: Expected a Dice Roll but found '%s'" % self.leftChild.string)
        if not isinstance(self.rightChild, Number):
            raise SyntaxError("REROLL SYNTAX ERROR: Expected a Number but found '%s'" % self.rightChild.string)
        reroll_number = self.rightChild.evaluate()
        self.leftChild.evaluate()
        numberOfSides = self.leftChild.numberOfSides
        if reroll_number > numberOfSides:
            raise ValueError("REROLL VALUE ERROR: Expected a Reroll Number less then the number of sides but found '%s'" % numberOfSides)
