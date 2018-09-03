import unittest
from challenge import find_shortest_distance


class TestChallenge(unittest.TestCase):
    def test_provided_case(self):
        text = "We do value and reward motivation in our development team. Development is a key skill for a DevOp."
        result = find_shortest_distance(text, "motivation", "development")
        self.assertEqual(2, result)

    def test_provided_case_repeated(self):
        text = "We do value and reward motivation in our development team motivation."
        result = find_shortest_distance(text, "motivation", "development")
        self.assertEqual(1, result)

    def test_provided_case_no_word(self):
        text = "Development is a key skill for a DevOp."
        result = find_shortest_distance(text, "motivation", "development")
        self.assertEqual(-1, result)

    def test_provided_case_shortened(self):
        text = "We do value and reward motivation in our motivation development team."
        result = find_shortest_distance(text, "motivation", "development")
        self.assertEqual(0, result)
