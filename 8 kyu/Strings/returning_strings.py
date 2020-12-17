"""Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

SQL: return results in a column named greeting

[Make sure you type the exact thing I wrote or the program may not execute properly]
    """

import unittest

def greet(name):
    #Good Luck (like you need it)
    return f"Hello, {name} how are you doing today?"


class TestReturningStrings(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet('Ryan'), "Hello, Ryan how are you doing today?")


if __name__ == "__main__":
    unittest.main()