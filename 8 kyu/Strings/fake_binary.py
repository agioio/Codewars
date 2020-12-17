"""Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

    """

import unittest

def fake_bin(x):
    return "".join("0" if int(char) < 5 else "1" for char in x)


class TestFakeBinary(unittest.TestCase):

    def test_fake_bin(self):
        tests = [
            ["01011110001100111", "45385593107843568"],
            ["101000111101101", "509321967506747"],
            ["011011110000101010000011011", "366058562030849490134388085"],
            ["01111100", "15889923"],
            ["100111001111", "800857237867"],
        ]
        for ans,inp in tests:
            self.assertEqual(fake_bin(inp),ans)
    

if __name__ == "__main__":
    unittest.main()