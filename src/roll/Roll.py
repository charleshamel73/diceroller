from src.operator.Operator import Operator


class Roll(Operator):
    numberOfDice = None
    numberOfSides = None
    rolls = []

    def dice_roll(self):
        raise Exception("Error: Roll Node must implement dice_roll()")

    def get_sum_of_roll(self):
        sum = 0
        for dice in self.rolls:
            sum += dice
        return sum