from unittest import TestCase
from src.parser.Parser import Parser


class TestParser(TestCase):
    parser = None

    def setUp(self):
        self.parser = Parser()
    #
    # def test_multiplication(self):
    #     self.parser.parse("2*5+5")
    #     roll = self.parser.roll()
    #     print roll
    #     self.parser.parse("5+5*2")
    #     roll = self.parser.roll()
    #     print roll

    # def test_dice_roll(self):
    #     self.parser.parse("2d4*5")
    #     roll = self.parser.roll()
    #     print roll
    #     self.parser.parse("5*2d4")
    #     roll = self.parser.roll()
    #     print roll

    def test_dice_roll(self):
        self.parser.parse("3d4r3")
        roll = self.parser.roll()
        print roll
        self.parser.parse("3d4k1L")
        roll = self.parser.roll()
        print roll
        self.parser.parse("3d4r3k1L")
        roll = self.parser.roll()
        print roll

        self.parser.parse("3d4k2Hr3")
        roll = self.parser.roll()
        print roll