"""Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
    """

import unittest

def areYouPlayingBanjo(name):
    # Implement me!
    if list(name)[0].lower() == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


class TestAreYouPlayingBanjo(unittest.TestCase):

    def test_areYouPlayingBanjo(self):
        self.assertEqual(areYouPlayingBanjo("martin"), "martin does not play banjo")
        self.assertEqual(areYouPlayingBanjo("Rikke"), "Rikke plays banjo")

if __name__ == "__main__":
    unittest.main()