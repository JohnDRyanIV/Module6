import unittest
from more_functions import string_functions


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(string_functions.multiply_string("Ayah, 3"), "AyahAyahAyah")
        self.assertEqual(string_functions.multiply_string("John, 4"), "JohnJohnJohnJohn")


if __name__ == '__main__':
    unittest.main()
