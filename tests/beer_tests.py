import unittest
from models.brewery import Brewery
from models.beer import Beer

class TestBeer(unittest.TestCase):
    def setUp(self):
        self.Brewery1 = Brewery("Newbarns")
        self.Brewery2 = Brewery("Moonwake")
        self.Beer1 = Beer("Turbo Shandy",5.0,self.Brewery1,1)
        self.Beer2 = Beer("Pale Ale",3.5,self.Brewery1,2)
        self.Beer3 = Beer("IPA",6.5,self.Brewery2,3)

    def test_has_name(self):
        result = self.Beer1.name
        self.assertEqual("Turbo Shandy",result)

    def test_has_abv(self):
        result = self.Beer1.abv
        self.assertEqual(5,result)

    def test_has_brewery(self):
        result = self.Beer2.brewery.name
        self.assertEqual("Newbarns",result)