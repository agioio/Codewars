"""Complete the solution so that it reverses all of the words within the string passed in.
    """

import unittest

def reverseWords(s):
    text = s.split()
    return " ".join(reversed(text))


class TestReversedWords(unittest.TestCase):

    def test_reverse_words(self):
        self.assertEqual(reverseWords("hello world!"), "world! hello")


if __name__ == "__main__":
    unittest.main()