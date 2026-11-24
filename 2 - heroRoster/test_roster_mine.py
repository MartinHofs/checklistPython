import os
import tempfile
import unittest

import roster

class TestRosterMine(unittest.TestCase):
    def setUp(self): # This method is called before each test. It creates a temporary directory and sets the path for the database file within that directory. It also creates the heroes table and adds four heroes to it.
        folder = tempfile.mkdtemp()
        self.db = os.path.join(folder, "test_guild.db")
        roster.create_table(self.db)
        roster.add_hero(self.db, "Brenna", "Warrior", 3)
        roster.add_hero(self.db, "Corwin", "Mage", 5)
        roster.add_hero(self.db, "Dax", "Rogue", 2)
        roster.add_hero(self.db, "Elsbeth", "Mage", 4)

    def test_heroes_by_level_highest_first(self): # This test checks if the heroes_by_level function returns the heroes sorted by level in descending order. It verifies that the returned list matches the expected order of heroes based on their levels.
        self.assertEqual(
            roster.heroes_by_level(self.db),
            [("Corwin", "Mage", 5), ("Elsbeth", "Mage", 4),
             ("Brenna", "Warrior", 3), ("Dax", "Rogue", 2)],
        )

    def test_heroes_in_role(self): # This test checks if the heroes_in_role function returns the correct list of heroes for a given role. It verifies that the returned list contains only the heroes with the role "Mage" and their respective levels.
        self.assertEqual(
            roster.heroes_in_role(self.db, "Mage"),
            [("Corwin", 5), ("Elsbeth", 4)],
        )