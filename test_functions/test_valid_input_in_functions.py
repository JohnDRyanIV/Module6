import unittest
from more_functions import validate_input_in_functions as h


class MyTestCase(unittest.TestCase):

    def test_score_input_test_name(self):
        self.assertEqual(h.score_input("Comp"), "Comp: 0")

    def test_score_input_test_score_valid(self):
        self.assertEqual(h.score_input("Comp", 90), "Comp: 90")

    def test_score_input_test_score_below_range(self):
        self.assertEqual(h.score_input("Comp", -50), "Invalid test score, try again")

    def test_score_input_test_score_above_range(self):
        self.assertEqual(h.score_input("Comp", 150), "Invalid test score, try again")

    def test_score_input_test_non_numeric(self):
        self.assertEqual(h.score_input("Comp", "!%$#@@#"), "Invalid test score, try again")

    def test_score_input_invalid_message(self):
        self.assertEqual(h.score_input("Comp", 150, "Incorrect input"), "Incorrect input")
        self.assertEqual(h.score_input("Comp", 50, "Incorrect input"), "Comp: 50")


if __name__ == '__main__':
    unittest.main()
