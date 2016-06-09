from src.modifier.Highest import Highest
from src.modifier.Lowest import Lowest
from src.operator.Roll import Roll
from src.operator.Operator import Operator
from src.operator.Reroll import Reroll


class Keep(Operator):
    symbol = "k"

    def evaluate(self):
        dice_roll = self.leftChild
        dice_count = self.rightChild.evaluate()
        rolls = dice_roll.rolls
        if isinstance(self.rightChild, Highest):
            rolls.sort()
        elif isinstance(self.rightChild, Lowest):
            rolls.sort(reverse=True)
        sum = 0
        for i in range(0, dice_count):
            sum += rolls[i]
        print "KEEP: %s with a sum of %s" % (self.string, sum)
        return sum

    def validate(self):
        self.leftChild.validate()
        self.rightChild.validate()
        if not isinstance(self.leftChild, (Reroll, Roll)):
            raise SyntaxError("KEEP SYNTAX ERROR: Expected a Dice Roll or Reroll on the left but found '%s'"%self.leftChild.string)
        if not isinstance(self.rightChild, (Highest, Lowest)):
            raise SyntaxError("KEEP SYNTAX ERROR: Expected a Highest or Lowest but found '%s'" % self.rightChild.string)
        dice_count = self.rightChild.evaluate()
        self.leftChild.evaluate()
        numberOfSides = self.leftChild.numberOfSides
        if dice_count > numberOfSides:
            raise ValueError("REROLL VALUE ERROR: Expected a Keep Count less then the number of dice rolled but found '%s'" % numberOfSides)
