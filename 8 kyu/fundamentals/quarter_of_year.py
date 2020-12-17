"""Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
    """

import unittest

def quarter_of(month):
    # your code here
    if 0 < month < 4:
        return 1
    elif 3 < month < 7:
        return 2
    elif 6 < month < 10:
        return 3
    else:
        return 4

class TestQuarterOfYear(unittest.TestCase):

    def test_quarter_of(self):
        self.assertEqual(quarter_of(3), 1)
        self.assertEqual(quarter_of(8), 3)
        self.assertEqual(quarter_of(11), 4)

    
if __name__ == "__main__":
    unittest.main()