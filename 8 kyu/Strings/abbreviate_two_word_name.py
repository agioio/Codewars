"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F
    """

import unittest

def abbrev_name(name):
    return f"{name.split()[0][0].upper()}.{name.split()[1][0].upper()}"


class TestAbbreviateName(unittest.TestCase):

    def test_abrrev_name(self):
        self.assertEqual(abbrev_name("Sam Harris"), "S.H")
        self.assertEqual(abbrev_name("Patrick Feenan"), "P.F")
        self.assertEqual(abbrev_name("Evan Cole"), "E.C")
        self.assertEqual(abbrev_name("P Favuzzi"), "P.F")
        self.assertEqual(abbrev_name("David Mendieta"), "D.M")


if __name__ == "__main__":
    unittest.main()