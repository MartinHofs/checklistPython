import unittest

import creatures

class TestCreaturesMine(unittest.TestCase):
    def test_creature_missing_health(self):
        with self.assertRaises(TypeError):
            creatures.Creature("Thing")  # Missing health argument

    def test_goblin_attack_value(self):
        g = creatures.Goblin("Grix")
        self.assertEqual(g.attack(), 4)  # This should pass, but if you change the attack method in Goblin, it will fail