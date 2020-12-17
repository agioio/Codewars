"""Complete the solution so that it reverses the string passed into it.
    """

import unittest

def solution(string):
    return string[::-1]


class TestReverseString(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution('world'), 'dlrow')
        self.assertEqual(solution('hello'), 'olleh')
        self.assertEqual(solution(''), '')
        self.assertEqual(solution('h'), 'h')

    
if __name__ == "__main__":
    unittest.main()