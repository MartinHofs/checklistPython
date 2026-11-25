# Write test_roster_mine.py: a class that extends unittest.TestCase and uses assertEqual to check a query result. For example: add two heroes of the same role to a temporary database and check what heroes_in_role returns, or check average_level after a level_up. Use a temporary database file, never guild.db.
# Break it on purpose: change one line of the program, run the provided tests, read the FAIL or ERROR report, name the test that caught it and the line it points to, then restore the line.

import os
import tempfile
import unittest

import roster

class TestRosterMine(unittest.TestCase):
    def setUp(self):
        # Create a temporary database file for testing
        self.temp_db_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_db_file.close()  # Close the file so that roster can use it
        self.roster = roster.Roster(self.temp_db_file.name)

    def tearDown(self):
        # Clean up the temporary database file after tests
        os.unlink(self.temp_db_file.name)

    def test_heroes_in_role(self):
        # Add two heroes of the same role to the temporary database
        self.roster.add_hero("Hero1", "Warrior", 5)
        self.roster.add_hero("Hero2", "Warrior", 3)

        # Check what heroes_in_role returns
        heroes = self.roster.heroes_in_role("Warrior")
        self.assertEqual(len(heroes), 2)
        self.assertIn("Hero1", [hero.name for hero in heroes])
        self.assertIn("Hero2", [hero.name for hero in heroes])

    def test_average_level_after_level_up(self):
        # Add a hero to the temporary database
        self.roster.add_hero("Hero3", "Mage", 2)

        # Level up the hero
        self.roster.level_up("Hero3")

        # Check average_level after level_up
        avg_level = self.roster.average_level()
        self.assertEqual(avg_level, 3)  # Hero3 should now be level 3