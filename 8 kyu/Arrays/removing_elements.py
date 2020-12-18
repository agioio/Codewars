"""Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
    
my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]

None of the arrays will be empty, so you don't have to worry about that!
    """

import unittest


def remove_every_other(my_list):
    # Your code here!
    return [my_list[ele] for ele in range(len(my_list)) if ele%2 == 0]

#return my_list[::2]


class TestRemoveElements(unittest.TestCase):

    def test_remove_every_other(self):
        self.assertEqual(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
                   [['Goodbye']])
        self.assertEqual(remove_every_other([[1, 2]]), [[1, 2]])
        self.assertEqual(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                   [1, 3, 5, 7, 9])
        self.assertEqual(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
                   ['Hello', 'Hello Again'])


if __name__ == "__main__":
    unittest.main()