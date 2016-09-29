import unittest

from minimum_payment import balance_after_12_minimum_payments

class TestMinimumPayment(unittest.TestCase):

    def test_case_one(self):
        self.assertEqual(
            {'Remaining balance': 31.38},
            balance_after_12_minimum_payments(42, 0.2, 0.04)
        )

    def test_case_two(self):
       self.assertEqual(
           {'Remaining balance': 361.61},
           balance_after_12_minimum_payments(484, 0.2, 0.04)
       )

    def test_case_three(self):
        self.assertEqual(
           {'Remaining balance': 3147.67},
           balance_after_12_minimum_payments(4213, 0.2, 0.04)
        )

    def test_case_four(self):
        self.assertEqual(
           {'Remaining balance': 3617.62},
           balance_after_12_minimum_payments(4842, 0.2, 0.04)
        )

if __name__ == '__main__':
    unittest.main()
