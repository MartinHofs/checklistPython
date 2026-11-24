import unittest

from guildtools import dice, loot

class TestDice(unittest.TestCase):
    def test_roll_stays_in_range(self):
        for _ in range(200):
            self.assertIn(dice.roll(6), range(1, 7))

    def test_roll_many_length(self):
        self.assertEqual(len(dice.roll_many(5, 20)), 5)

    def test_roll_many_values_in_range(self):
        for value in dice.roll_many(100, 4):
            self.assertIn(value, [1, 2, 3, 4])

    def test_dice_functions_have_docstrings(self):
        self.assertTrue(dice.roll.__doc__)
        self.assertTrue(dice.roll_many.__doc__)