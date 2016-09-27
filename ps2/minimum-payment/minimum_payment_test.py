import unittest

from minimum_payment import calculate_minimum_payment

class TestMinimumPayment(unittest.TestCase):

    def test_case_one(self):
        self.assertEqual(
            {'Remaining balance': 31.38},
            calculate_minimum_payment(42, 0.2, 0.04)
        )

    def test_case_two(self):
       self.assertEqual(
           {'Remaining balance': 361.61},
           calculate_minimum_payment(484, 0.2, 0.04)
       )

    def test_case_three(self):
        self.assertEqual(
           {'Remaining balance': 3147.67},
           calculate_minimum_payment(4213, 0.2, 0.04)
        )

    def test_case_four(self):
        self.assertEqual(
           {'Remaining balance': 3617.62},
           calculate_minimum_payment(4842, 0.2, 0.04)
        )

if __name__ == '__main__':
    unittest.main()
