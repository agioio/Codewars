"""Write a function getDrinkByProfession/get_drink_by_profession() that receives as input parameter a string, and produces outputs according to the following table:

Input	                    Output
"Jabroni"	                "Patron Tequila"
"School Counselor"	        "Anything with Alcohol"
"Programmer"	            "Hipster Craft Beer"
"Bike Gang Member"     	    "Moonshine" 
"Politician"	            "Your tax dollars" 
"Rapper"	                "Cristal" 
*anything else*	            "Beer"

Note: anything else is the default case: if the input to the function is not any of the values in the table, then the return value should be "Beer."

Make sure you cover the cases where certain words do not show up with correct capitalization. For example, getDrinkByProfession("pOLitiCIaN") should still return "Your tax dollars".
    """

import unittest

def get_drink_by_profession(param):
    # code me!
    drink = {
        "jabroni":"Patron Tequila",
        "school counselor":"Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
    return drink.get(param.lower(),"Beer")


class TestBartenderDrinks(unittest.TestCase):

    def test_get_drink_by_profession(self):
        self.assertEqual(get_drink_by_profession("jabrOni"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")
        self.assertEqual(get_drink_by_profession("scHOOl counselor"), "Anything with Alcohol", "'School Counselor' should map to 'Anything with alcohol'")
        self.assertEqual(get_drink_by_profession("prOgramMer"), "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'")
        self.assertEqual(get_drink_by_profession("bike ganG member"), "Moonshine", "'Bike Gang Member' should map to 'Moonshine'")
        self.assertEqual(get_drink_by_profession("poLiTiCian"), "Your tax dollars", "'Politician' should map to 'Your tax dollars'")
        self.assertEqual(get_drink_by_profession("rapper"), "Cristal", "'Rapper' should map to 'Cristal'")
        self.assertEqual(get_drink_by_profession("pundit"), "Beer", "'Pundit' should map to 'Beer'")
        self.assertEqual(get_drink_by_profession("Pug"), "Beer", "'Pug' should map to 'Beer'")

if __name__ == "__main__":
    unittest.main()