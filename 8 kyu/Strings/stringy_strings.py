"""write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.
    """
import unittest

def stringy(size):
    # Good Luck!
    lst = []
    for i in range(size):
        if i % 2 == 0:
            lst.append("1")
        else:
            lst.append("0")
    return "".join(lst)


class TestStringyStrings(unittest.TestCase):

    def test_stringy(self):
        self.assertEqual(stringy(26), '10101010101010101010101010', 'oops try again')
        self.assertEqual(stringy(28), '1010101010101010101010101010', 'oops try again')
        self.assertEqual(stringy(10)[0],'1',"Whoops your string doesn't start with a '1'")
        self.assertEqual(stringy(3), '101', 'oops try again')

if __name__ == "__main__":
    unittest.main()