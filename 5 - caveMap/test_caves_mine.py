# Write test_caves_mine.py: a class that extends unittest.TestCase, builds a small cave of its own (at least three rooms), and uses assertIs to check that find_room returns None for a room that is not there. Add a second test of its own.
# Break it on purpose: change one line of the program, run the provided tests, read the FAIL or ERROR report, name the test that caught it and the line it points to, then restore the line.


import unittest

import caves


def room(name, gold, tunnels=None):
    return {"name": name, "gold": gold, "tunnels": tunnels or []}

class TestCavesMine(unittest.TestCase):
    def setUp(self):
        self.my_cave = room("Main", 0, [
            room("Side Room 1", 10),
            room("Side Room 2", 20, [room("Deep Room", 100)]),
        ])

    def test_find_room_missing(self):
        self.assertIs(caves.find_room(self.my_cave, "Nonexistent Room"), None)

    def test_total_gold_my_cave(self):
        self.assertEqual(caves.total_gold(self.my_cave), 130)