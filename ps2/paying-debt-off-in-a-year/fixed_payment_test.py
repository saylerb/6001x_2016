import unittest

from fixed_payment import calculate_monthly_payment

class TestFixedPayment(unittest.TestCase):

    def test_case_one(self):
        self.assertEqual(
            {'Lowest payment': 310},
            calculate_monthly_payment(3329, 0.2)
        )

    def test_case_two(self):
       self.assertEqual(
           {'Lowest payment': 440},
           calculate_monthly_payment(4773, 0.2)
       )

    def test_case_three(self):
        self.assertEqual(
           {'Lowest payment': 360},
           calculate_monthly_payment(3926, 0.2)
        )

if __name__ == '__main__':
    unittest.main()
