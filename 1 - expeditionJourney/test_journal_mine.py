from ast import Break

import os
import tempfile
import unittest

import journal

class TestJournalMine(unittest.TestCase):
    def setUp(self): # This method is called before each test. It creates a temporary directory and sets the path for the journal file within that directory.
        folder = tempfile.mkdtemp()
        self.path = os.path.join(folder, "journal.txt")

    def test_add_entry_with_space_in_place_name(self): # This test checks if the add_entry function can handle place names that contain spaces. It adds an entry with a place name "Crystal Gallery" and verifies that the entry is correctly written to the journal file.
        journal.add_entry(self.path, "Crystal Gallery", 40)
        with open(self.path) as f:
            self.assertEqual(f.read(), "Crystal Gallery,40\n")

    def test_total_gold_after_three_entries(self): # This test checks if the total_gold function correctly calculates the total amount of gold after adding three entries to the journal. It adds entries for "Mushroom Hall", "Echo Chamber", and "Crystal Gallery" with respective gold amounts of 15, 5, and 40, and then verifies that the total gold is 60.
        journal.add_entry(self.path, "Mushroom Hall", 15)
        journal.add_entry(self.path, "Echo Chamber", 5)
        journal.add_entry(self.path, "Crystal Gallery", 40)
        self.assertEqual(journal.total_gold(self.path), 60)

if __name__ == "__main__":
    unittest.main()