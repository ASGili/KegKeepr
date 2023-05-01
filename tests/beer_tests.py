import unittest
from models.brewery import Brewery
from models.beer import Beer

class TestBeer(unittest.TestCase):
    def setUp(self):
        self.brewery1 = Brewery("Newbarns")
        self.brewery2 = Brewery("Moonwake")
        self.beer1 = Beer("Turbo Shandy",5.0,self.brewery1,1)
        self.beer2 = Beer("Pale Ale",3.5,self.brewery1,2)
        self.beer3 = Beer("IPA",6.5,self.brewery2,3)

    def test_has_name(self):
        result = self.beer1.name
        self.assertEqual("Turbo Shandy",result)

    def test_has_abv(self):
        result = self.beer1.abv
        self.assertEqual(5,result)

    def test_has_brewery(self):
        result = self.beer2.brewery.name
        self.assertEqual("Newbarns",result)