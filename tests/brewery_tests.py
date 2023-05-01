import unittest

from models.brewery import Brewery

class TestBrewery(unittest.TestCase):
    def setUp(self):
        self.brewery1 = Brewery("Newbarns")
        self.brewery2 = Brewery("Moonwake")

    def test_has_name(self):
        result = self.rewery1.name
        self.assertEqual("Newbarns",result)

    