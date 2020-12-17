"""Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.
    """

import unittest

def is_digit(n):
    return n.isdigit()

class TestIsItADigit(unittest.TestCase):

    def test_is_digit(self):
        self.assertEqual(is_digit(""), False)
        self.assertEqual(is_digit("7"), True)
        self.assertEqual(is_digit(" "), False)
        self.assertEqual(is_digit("a"), False)
        self.assertEqual(is_digit("a5"), False)

if __name__ == "__main__":
    unittest.main()