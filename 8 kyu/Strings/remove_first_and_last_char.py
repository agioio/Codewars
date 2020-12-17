"""It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
    """

import unittest

def remove_char(s):
    #your code here
    return s[1:-1:1]


class TestRemoveFirstLastChar(unittest.TestCase):

    def test_remove_char(self):
        self.assertEqual(remove_char('eloquent'), 'loquen')
        self.assertEqual(remove_char('country'), 'ountr')
        self.assertEqual(remove_char('person'), 'erso')
        self.assertEqual(remove_char('place'), 'lac')
        self.assertEqual(remove_char('ok'), '')


if __name__ == "__main__":
    unittest.main()