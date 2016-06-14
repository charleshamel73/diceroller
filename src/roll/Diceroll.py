import random
from src.roll.Roll import Roll


class Diceroll(Roll):
    symbol = "d"

    def rollDice(self):
        self.numberOfDice = self.leftChild.getValue()
        self.numberOfSides = self.rightChild.getValue()
        self.rolls = []
        for i in range(0, self.numberOfDice):
            roll = random.randint(1, self.numberOfSides)
            self.rolls.append(roll)
        return self.rolls

    def get_sum_of_roll(self):
        sum = 0
        for dice in self.rolls:
            sum += dice
        return sum
