"""Your goal is to return multiplication table for number that is always an integer from 1 to 10.

For example, a multiplication table (string) for number == 5 looks like below:
    """

import unittest

def multi_table(number):
    text = []
    text.append(f"1 * {number} = {1*number}")
    for i in range(2,11):
        text.append(f"\n{i} * {number} = {i*number}")
        
    return "".join(text) # good luck


class TestMultiplactionTable(unittest.TestCase):

    def test_multi_table(self):
        self.assertEqual(multi_table(5), '1 * 5 = 5\n2 * 5 = 10\n3 * 5 = 15\n4 * 5 = 20\n5 * 5 = 25\n6 * 5 = 30\n7 * 5 = 35\n8 * 5 = 40\n9 * 5 = 45\n10 * 5 = 50')
        self.assertEqual(multi_table(1), '1 * 1 = 1\n2 * 1 = 2\n3 * 1 = 3\n4 * 1 = 4\n5 * 1 = 5\n6 * 1 = 6\n7 * 1 = 7\n8 * 1 = 8\n9 * 1 = 9\n10 * 1 = 10')


if __name__ == "__main__":
    unittest.main()