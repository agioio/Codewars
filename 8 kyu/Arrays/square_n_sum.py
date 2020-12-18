"""Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
    """
import unittest


def square_sum(numbers):
    #your code here
    return sum(num**2 for num in numbers)


class TestSquareNSum(unittest.TestCase):

    def test_square_sum(self):
        self.assertEqual(square_sum([1,2]), 5)
        self.assertEqual(square_sum([0, 3, 4, 5]), 50)


if __name__ == "__main__":
    unittest.main()