"""This kata is from check py.checkio.org

You are given an array with positive numbers and a non-negative number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

Let's look at a few examples:

array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.
    """
import unittest

def index(array, n):
    try:
        return array[n]**n
    except:
        return -1


class TestIndexPower(unittest.TestCase):

    def test_index(self):
        self.assertEqual(index([1, 2, 3, 4],2),9)
        self.assertEqual(index([1, 3, 10, 100],3),1000000)

if __name__ == "__main__":
    unittest.main()