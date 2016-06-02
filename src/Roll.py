import random
from Node import Node
from src.Number import Number


class Roll(Node):
    symbol = "d"
    string = ""
    numberOfDice = None
    numberOfSides = None
    redo = None
    keep = None

    def __init__(self, string):
        from src.NodeFactory import NodeFactory
        start_index = 0
        d_index = string.find('d')
        r_index = string.find('r')
        k_index = string.find('k')
        self.numberOfDice = Number(string[start_index:d_index])
        #Entry that use both keep and reroll, enforces that reroll is before keep
        if r_index != -1 and k_index != -1 and r_index > k_index:
            raise Exception("ROLL SYNTAX ERROR: found '%s' but reroll(r) should be before keep(k)"%string)
        #Gets the number of Sides taking into account any mods
        if r_index == -1 and k_index == -1:
            self.numberOfSides = Number(string[d_index + 1:])
        elif r_index != -1:
            self.numberOfSides = Number(string[d_index + 1:r_index])
        elif k_index != -1:
            self.numberOfSides = Number(string[d_index + 1:k_index])
        # getting modifiers.
        if r_index != -1 and k_index == -1:
            self.redo = Number(string[r_index + 1:])
        elif r_index == -1 and k_index != -1:
            self.keep = NodeFactory.fetch_part(string[k_index + 1:])
        elif r_index != -1 and k_index != -1:
            self.redo = Number(string[r_index + 1:k_index])
            self.keep = NodeFactory.fetch_value(string[k_index + 1:])
        self.string = string
        if self.numberOfDice.evaluate() <= 0:
            raise ValueError("ROLL VALUE ERROR: Number of Dice must be greater than 0. Found '%s'"%string)
        if self.numberOfSides.evaluate() <= 0:
            raise ValueError("ROLL VALUE ERROR: Sides of the Dice must be greater than 0. Found '%s'" % string)
        if self.keep is not None and self.keep.evaluate() > self.numberOfDice.evaluate():
            raise ValueError("ROLL VALUE ERROR: Number of dice kept can't be greater then the number of dice rolled. Found '%s'" % string)
        if self.keep is not None and self.keep.evaluate() <= 0:
            raise ValueError("ROLL VALUE ERROR: number of dice to keep must be greater than 0. Found '%s'" % string)
        if self.redo is not None and self.redo.evaluate() > self.numberOfSides.evaluate():
            raise ValueError("ROLL VALUE ERROR: number to reroll on cannot be greater then the number of sides of the dice. Found '%s'" % string)
        if self.redo is not None and self.redo.evaluate() <= 0:
            raise ValueError("ROLL VALUE ERROR: number to reroll on must be greater than 0. Found '%s'" % string)

    def evaluate(self):
        # ROLL THE DICE X TIMES ADD IT TO LIST
        # IF the number matches then redo roll
        # AT END SORT LIST BY ASCEND OR DESCEND AND DROP LAST X
        rolls = []
        for i in range(0, self.numberOfDice.evaluate()):
            if self.redo is not None:
                roll = self.redo.evaluate()
                while roll == self.redo.evaluate():
                    roll = random.randint(1, self.numberOfSides.evaluate());
            else:
                roll = random.randint(1, self.numberOfSides.evaluate());
            rolls.append(roll)
        # Sort list according to Keep
        dice_count = self.numberOfDice.evaluate()
        if self.keep is not None:
            type_name = self.keep.__class__.__name__
            dice_count = self.keep.evaluate()
            if type_name == "Lowest":
                rolls.sort()
            else:
                rolls.sort(reverse=True)
        sum_of_rolls = 0;
        for i in range(0, dice_count):
            sum_of_rolls += rolls[i]
        print "rolls for '%s': %s with a sum of %s"%(self.string, rolls, sum_of_rolls)
        return sum_of_rolls
