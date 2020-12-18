"""You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
    """

import unittest


def positive_sum(arr):
    # Your code here
    return sum(num for num in arr if num > 0)


class TestSumOfPositive(unittest.TestCase):

    def test_positive_sum(self):
        self.assertEqual(positive_sum([1,2,3,4,5]),15)
        self.assertEqual(positive_sum([1,-2,3,4,5]),13)
        self.assertEqual(positive_sum([-1,2,3,4,-5]),9)
        self.assertEqual(positive_sum([]),0)
        self.assertEqual(positive_sum([-1,-2,-3,-4,-5]),0)


if __name__ == "__main__":
    unittest.main()