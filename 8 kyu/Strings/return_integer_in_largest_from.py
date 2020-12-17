"""Write a function that rearranges an integer into its largest possible value.
    """
import unittest

def super_size(n):
    #your code here
    return int("".join(sorted(str(n),reverse=True)))


class TestLargestForm(unittest.TestCase):

    def test_super_size(self):
        self.assertEqual(super_size(69),96)
        self.assertEqual(super_size(513),531)
        self.assertEqual(super_size(2017),7210)
        self.assertEqual(super_size(414),441)
        self.assertEqual(super_size(608719),987610)
        self.assertEqual(super_size(700000000001),710000000000)
        self.assertEqual(super_size(0),0)


if __name__ == "__main__":
    unittest.main()