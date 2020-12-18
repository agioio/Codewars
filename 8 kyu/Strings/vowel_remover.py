"""Create a function called shortcut to remove all the lowercase vowels in a given string.


shortcut("codewars") # --> cdwrs
shortcut("goodbye")  # --> gdby
    """
import unittest


def shortcut(s):
    return ''.join(char for char in s if char not in 'aeiou')


#def shortcut(s):
    # return s.translate(None, 'aeiou')


class TestVowelRemover(unittest.TestCase):

    def test_shortcut(self):
        for t in [
            ["hello","hll"],
            ["hellooooo","hll"],
            ["how are you today?","hw r y tdy?"],
            ["complain","cmpln"],
            ["never","nvr"]
        ]:
            ans,exp = shortcut(t[0]),t[1]
            self.assertEqual(ans,exp)
    

if __name__ == "__main__":
    unittest.main()