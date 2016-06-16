import random
from src.roll.Roll import Roll


class Diceroll(Roll):
    symbol = "d"

    def dice_roll(self):
        self.numberOfDice = self.leftChild.getValue()
        self.numberOfSides = self.rightChild.getValue()
        self.rolls = []
        for i in range(0, self.numberOfDice):
            roll = random.randint(1, self.numberOfSides)
            self.rolls.append(roll)
        return self.rolls