import unittest

from models.brewery import Brewery

class TestBrewery(unittest.TestCase):
    def setUp(self):
        self.Brewery1 = Brewery("Newbarns")
        self.Brewery2 = Brewery("Moonwake")

    def test_has_name(self):
        result = self.Brewery1.name
        self.assertEqual("Newbarns",result)

    