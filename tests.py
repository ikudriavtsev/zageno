import unittest
from challenge import find_shortest_distance


class TestChallenge(unittest.TestCase):
    def test_provided_case(self):
        text = "We do value and reward motivation in our development team. Development is a key skill for a DevOp."
        result = find_shortest_distance(text, "motivation", "development")
        self.assertEqual(2, result)
