import unittest

from closest_power import get_closest_power

class ClosestPowerTest(unittest.TestCase):
    def test_case_numero_uno(self):
        self.assertEqual(2, get_closest_power(3, 12))

    def test_case_numero_dos(self):
        self.assertEqual(2, get_closest_power(4, 12))

    def test_case_numero_tres(self):
        self.assertEqual(0, get_closest_power(4, 1))

    def test_case_numero_quatro(self):
        self.assertEqual(7, get_closest_power(2, 192.0))

    def test_case_numero_cinco(self):
        self.assertEqual(3, get_closest_power(5, 375.0))

if __name__ == '__main__':
    unittest.main()
