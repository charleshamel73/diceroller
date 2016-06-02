import random

from src.parser.Operator import Operator
from src.parser.PartFactory import PartFactory


class Roll(Operator):
    symbol = "d"
    numberOfDice = 0
    numberOfSides = 0
    redo = 0
    keep = ""
    def __init__(self, string):
        self.string = string
        #PARSE (4)d(5r6Lk)
        parts = string.split(self.symbol, 1)
        self.numberOfDice = int(parts[0])
        # 5r6Lk
        key = ""
        value = ""
        for char in parts[1]:
            if key == "":
                if char =="r" or char =="k":
                    self.numberOfSides = int(value)
                    key = char
                    value = ""
                else:
                    value += char
            #r6Lk3
            elif key == "r":
                if char == "k":
                    self.redo = int(value)
                    key = char
                    value = ""
                else:
                    value +=char
            elif key == "k":
                if char == "r":
                    self.keep = PartFactory.fetch_part(value)
                    key = char
                    value = ""
                else:
                    value += char
        #ADDS VALUE WHEN END OF FILE
        if key == "" and value != "":
            self.numberOfSides = int(value)
        if key == "r" and value != "":
            self.redo = PartFactory.fetch_part(value)
        elif key == "k" and value != "":
            self.keep = PartFactory.fetch_part(value)

    def evaluate(self):
        #ROLL THE DICE X TIMES ADD IT TO LIST
        #IF the number matches then redo roll
        #AT END SORT LIST BY ASCEND OR DESCEND AND DROP LAST X
        rolls = []
        for i in range(0, self.numberOfDice):
            if(self.redo != 0):
                roll = self.redo
                while self.redo != 0 and roll == self.redo:
                    roll = random.randint(1, self.numberOfSides);
                    if roll == self.redo:
                        print "ROLLED A %s: REROLLING DIE" % self.redo
            else:
                roll = random.randint(1, self.numberOfSides);
            rolls.append(roll)
            print "roll %s: %s" % (i + 1, roll)
        print "BEFORE: %s"%rolls
        # Sort list according to Keep
        diceCount = self.numberOfDice
        if self.keep != "":
            type_name = self.keep.__class__.__name__
            diceCount = self.keep.evaluate()
            if type_name == "Lowest":
                print "SORTED BY LOWEST -> HIGHEST"
                rolls.sort()
            else:
                print "SORTED BY HIGHEST -> LOWEST"
                rolls.sort(reverse=True)
            print "Number of Dice saved: %s" % (diceCount)
        print "AFTER: %s"%rolls
        sum = 0;
        for i in range(0,diceCount):
            sum+= rolls[i]
        return sum