import random
from src.roll.Roll import Roll


class Reroll(Roll):
    symbol = "r"
    reroll = -1

    def dice_roll(self):
        left_roll = self.leftChild
        self.numberOfSides = left_roll.numberOfSides
        self.numberOfDice = left_roll.numberOfDice
        self.reroll = self.rightChild.getValue()
        self.rolls = []
        for roll in left_roll.rolls:
            while roll == self.reroll:
                roll = random.randint(1, self.numberOfSides)
            self.rolls.append(roll)
