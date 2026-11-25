# Write test_guildtools_mine.py: a class that extends unittest.TestCase and uses assertIsInstance (for example, a roll is an int, and roll_many returns a list) or assertIn (for example, a bonus is one of the six allowed values), with two tests of its own.
# Break it on purpose: change one line of the program, run the provided tests, read the FAIL or ERROR report, name the test that caught it and the line it points to, then restore the line.


import unittest

from guildtools import dice, loot

class TestDice(unittest.TestCase):
    def test_roll(self):
        result = dice.roll(6)
        self.assertIsInstance(result, int)
        self.assertIn(result, range(1, 7))

    def test_roll_many(self):
        result = dice.roll_many(3, 6)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        for roll in result:
            self.assertIsInstance(roll, int)
            self.assertIn(roll, range(1, 7))