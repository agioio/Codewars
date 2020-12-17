"""For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.
    """

import unittest

def well(x):
    # your code here
    if 0 < x.count("good") < 3: return "Publish!"
    elif x.count("good") >= 3: return "I smell a series!"
    else: return "Fail!"


class TestWellOfIdeas(unittest.TestCase):

    def test_well(self):
        self.assertEqual(well(['bad', 'bad', 'bad']), 'Fail!')
        self.assertEqual(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
        self.assertEqual(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')


if __name__ == "__main__":
    unittest.main()