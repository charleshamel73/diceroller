from src.modifier.Highest import Highest
from src.modifier.Lowest import Lowest
from src.roll.Roll import Roll


class Keep(Roll):
    symbol = "k"
    keep_count = -1

    def dice_roll(self):
        left_roll = self.leftChild
        self.numberOfSides = left_roll.numberOfSides
        self.numberOfDice = left_roll.numberOfDice
        self.rolls = left_roll.rolls
        self.keep_count = self.rightChild.getValue()
        if isinstance(self.rightChild, Highest):
            self.rolls.sort()
        elif isinstance(self.rightChild, Lowest):
            self.rolls.sort(reverse=True)
        self.rolls = self.rolls[:self.keep_count]
