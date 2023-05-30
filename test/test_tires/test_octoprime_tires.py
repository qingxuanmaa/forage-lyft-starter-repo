import unittest
from tire.octoprime_tire import Octoprime

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.7, 0.8, 0.8, 0.9]
        tires = Octoprime(tire_wear)
        self.assertTrue(tires.needs_service())
        
    def test_needs_service_false(self):
        tire_wear = [0.5, 0.3, 0.1, 0.5]
        tires = Octoprime(tire_wear)
        self.assertFalse(tires.needs_service())
