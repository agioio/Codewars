"""Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included).
    """
import unittest, re

def validate_usr(username):
    #your code here
    return re.match('^[a-z0-9_]{4,16}$',username) != None


class TestSimpleUsernameValidation(unittest.TestCase):

    def test_validate_usr(self):
        self.assertEqual(validate_usr('asddsa'), True)
        self.assertEqual(validate_usr('a'), False)
        self.assertEqual(validate_usr('Hass'), False)
        self.assertEqual(validate_usr('Hasd_12assssssasasasasasaasasasasas'), False)
        self.assertEqual(validate_usr(""),False)
        self.assertEqual(validate_usr('____'), True)
        
if __name__ == "__main__":
    unittest.main()