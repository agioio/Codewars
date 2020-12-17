"""Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to milliseconds.

"""

import unittest

def past(h, m, s):
    # Good Luck!
    # h = hour
    # m = minute
    return (h*3.6e+6 + m * 60000 + s * 1000)


class TestTimeClock(unittest.TestCase):

    def test_past(self):
        self.assertEqual(past(0,1,1),61000)
        self.assertEqual(past(1,1,1),3661000)
        self.assertEqual(past(0,0,0),0)
        self.assertEqual(past(1,0,1),3601000)
        self.assertEqual(past(1,0,0),3600000)
    

if __name__ == "__main__":
    unittest.main()