from unittest import TestCase

import mock

from src.main.Parser import Parser


@mock.patch('random.randint', return_value=3)
class TestParser(TestCase):
    def test_double_dice_roll(self, mocked_roll):
        parser = Parser()
        self.assertEqual(parser.parse("2d4+3d5"), 15)

    def test_mulitply(self, mocked_roll):
        parser = Parser()
        self.assertEqual(parser.parse("2d4*4"), 24)

    def test_divide(self, mocked_roll):
        parser = Parser()
        self.assertEqual(parser.parse("2d4/6"), 1)

    def test_subtract(self, mocked_roll):
        parser = Parser()
        self.assertEqual(parser.parse("2d4-2"), 4)

    def test_addition(self, mocked_roll):
        parser = Parser()
        self.assertEqual(parser.parse("2d4+5"), 11)

    def test_constants(self, mocked_roll):
        parser = Parser()
        self.assertEqual(parser.parse("4"), 4)
        self.assertEqual(parser.parse("4+3"), 7)
        self.assertEqual(parser.parse("4-3"), 1)
        self.assertEqual(parser.parse("6/3"), 2)
        self.assertEqual(parser.parse("4*3"), 12)

    def test_dice_roll(self, mocked_roll):
        parser = Parser()
        self.assertEqual(parser.parse("3d4"), 9)

    def test_negative_roll(self, mocked_roll):
        parser = Parser()
        self.assertRaises(SyntaxError,lambda:parser.parse("-3d4"))
        self.assertRaises(SyntaxError,lambda:parser.parse("3d-4"))
        self.assertRaises(SyntaxError,lambda:parser.parse("-3d4-4"))


    def test_mod(self,mocked_roll):
        parser = Parser()
        self.assertEqual(parser.parse("3d4"),9)
        self.assertEqual(parser.parse("3d4k2H"),6)
        self.assertEqual(parser.parse("3d4r4"),9)
        self.assertEqual(parser.parse("3d4r4k2H"),6)

    def test_negative_mod(self, mocked_roll):
        parser = Parser()
        self.assertRaises(SyntaxError,lambda: parser.parse("3d3k4Hr2"))
        self.assertRaises(ValueError,lambda:parser.parse("0d4k2H"))
        self.assertRaises(ValueError,lambda:parser.parse("3d0k2H"))
        self.assertRaises(ValueError, lambda: parser.parse("3d3k0L"))
        self.assertRaises(ValueError,lambda: parser.parse("3d3k4H"))
        self.assertRaises(ValueError, lambda: parser.parse("3d3r0k2L"))
        self.assertRaises(ValueError, lambda: parser.parse("3d3k2Lr0"))

    #TODO: ADD TEST FOR SORTED SUCH THAT 3L AND 5H
    #TODO: ADD CUSTOM EXCEPTION CLASSES AND FIX TEST