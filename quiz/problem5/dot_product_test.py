import unittest

from dot_product import calculate_dot_product

class DotProductTest(unittest.TestCase):
    def test_case_one(self):
        a, b = [1, 2, 3], [4, 5, 6]
        self.assertEqual(32, calculate_dot_product(a, b))

    def test_case_two(self):
        a, b = [38, 16, -14, -78, -72], [41, 11, -62, 84, -61]
        self.assertEqual(442, calculate_dot_product(a, b))

    def test_case_three(self):
        a = [39, 11, 89, 17, 23, 1, -100, 79, 53]
        b = [92, -9, 75, 4, 70, -55, 7, 55, -16]
        self.assertEqual(14584, calculate_dot_product(a, b))

if __name__ == '__main__':
    unittest.main()

