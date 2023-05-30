import unittest
from tire.carrigan_tire import Carrigan

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.3, 0.6, 0.1, 0.9]
        tires = Carrigan(tire_wear)
        self.assertTrue(tires.needs_service())
        
    def test_needs_service_false(self):
        tire_wear = [0.3, 0.2, 0.1, 0.8]
        tires = Carrigan(tire_wear)
        self.assertFalse(tires.needs_service())
        