"""Objective
Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.

array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
    """

import unittest


def array_madness(a,b):
    # Ready, get, set, GO!!!
    return sum(num**2 for num in a) > sum(num**3 for num in b)


class TestSpeedCode2Madness(unittest.TestCase):

    def test_array_madness(self):
        self.assertEqual(array_madness( [1, 2, 3],[4, 5, 6]),False)
        self.assertEqual(array_madness([4, 5, 6], [1, 2, 3]),True)


if __name__ == "__main__":
    unittest.main()