import unittest
from models.brewery import Brewery
from models.beer import Beer
from models.keg import Keg

class TestKeg(unittest.TestCase):
    def setUp(self):
        self.brewery1 = Brewery("Newbarns",1)
        self.brewery2 = Brewery("Moonwake",2)
        self.beer1 = Beer("Turbo Shandy",5.0,self.brewery1,1)
        self.beer2 = Beer("Pale Ale",3.5,self.brewery1,2)
        self.beer3 = Beer("IPA",6.5,self.brewery2,3)
        self.keg1 = Keg(self.beer2,80,1)
        self.keg2 = Keg(self.beer2,80,2)

    def test_has_beer(self):
        result = self.keg1.beer.name
        self.assertEqual("Pale Ale",result)

    