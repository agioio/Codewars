"""You're on your way to the market when you hear beautiful music coming from a nearby street performer. The notes come together like you wouln't believe as the musician puts together patterns of tunes. As you wonder what kind of algorithm you could use to shift octaves by 8 pitches or something silly like that, it dawns on you that you have been watching the musician for some 10 odd minutes. You ask, "How much do people normally tip for something like this?" The artist looks up. "Its always gonna be about tree fiddy."

It was then that you realize the musician was a 400 foot tall beast from the paleolithic era. The Loch Ness Monster almost tricked you!

There are only 2 guaranteed ways to tell if you are speaking to The Loch Ness Monster: A.) It is a 400 foot tall beast from the paleolithic era B.) It will ask you for tree fiddy

Since Nessie is a master of disguise, the only way accurately tell is to look for the phrase "tree fiddy". Since you are tired of being grifted by this monster, the time has come to code a solution for finding The Loch Ness Monster. Note: It can also be written as 3.50 or three fifty.
    """
import unittest,re 


def is_lock_ness_monster(string):
    #your code here
    return True if re.search(r"tree fiddy|3\.50",string) else False


class TestStrangeTripToMarket(unittest.TestCase):

    def test_is_lock_ness_monster(self):
        self.assertEqual(is_lock_ness_monster("Your girlscout cookies are ready to ship. Your total comes to tree fiddy"), True)
        self.assertEqual(is_lock_ness_monster("Howdy Pardner. Name's Pete Lexington. I reckon you're the kinda stiff who carries about tree fiddy?"),True)
        self.assertEqual(is_lock_ness_monster("I'm from Scottland. I moved here to be with my family sir. Please, $3.50 would go a long way to help me find them"),True)
        self.assertEqual(is_lock_ness_monster("Yo, I heard you were on the lookout for Nessie. Let me know if you need assistance."), False)
        self.assertEqual(is_lock_ness_monster("I will absolutely, positively, never give that darn Lock Ness Monster any of my three dollars and fifty cents"),False)
        self.assertEqual(is_lock_ness_monster("Did I ever tell you about my run with that paleolithic beast? He tried all sorts of ways to get at my three dolla and fitty cent? I told him 'this is MY 4 dolla!'. He just wouldn't listen."),False)
        self.assertEqual(is_lock_ness_monster("Hello, I come from the year 3150 to bring you good news!"),False)
        self.assertEqual(is_lock_ness_monster("By 'tree fiddy' I mean 'three fifty'"), True)
        self.assertEqual(is_lock_ness_monster("I will be at the office by 3:50 or maybe a bit earlier, but definitely not before 3, to discuss with 50 clients"),False)
        self.assertEqual(is_lock_ness_monster(""),False)


if __name__ == "__main__":
    unittest.main()