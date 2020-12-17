"""Alan is known for referring to the temperature of the apple turnover as 'Hotter than the sun!'. According to space.com the temperature of the sun's corona is 2,000,000 degrees C, but we will ignore the science for now.

Your job is simple, if (x) squared is more than 1000, return 'It's hotter than the sun!!', else, return 'Help yourself to a honeycomb Yorkie for the glovebox.'.

X will be either a number or a string. Both are valid.
    """

import unittest


def apple(x):
    return "It's hotter than the sun!!" if int(x)**2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."


class TestAppleTurnover(unittest.TestCase):

    def test_apple(self):
        self.assertEqual(apple('50'), "It's hotter than the sun!!")
        self.assertEqual(apple(4), "Help yourself to a honeycomb Yorkie for the glovebox.")
        self.assertEqual(apple("12"), "Help yourself to a honeycomb Yorkie for the glovebox.")
        self.assertEqual(apple(60), "It's hotter than the sun!!")


if __name__ == "__main__":
    unittest.main()