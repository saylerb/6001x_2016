import unittest

from bisection_search_payment import BisectPaymentCalculator

class TestBisectPaymentCalculator(unittest.TestCase):
    def test_it_has_attributes(self):
        calculator = BisectPaymentCalculator(balance = 100, annual_interest_rate = 0.02)
        self.assertEqual(100.0, calculator.initial_balance)
        self.assertEqual(0.02, calculator.annual_interest_rate)

    def test_it_generates_a_low_guess(self):
        calculator = BisectPaymentCalculator(balance = 600, annual_interest_rate = 0.02)
        result = calculator.initial_low
        self.assertIs(float, type(result))
        self.assertEqual(50.0, result)

    def test_it_generates_a_high_guess(self):
        calculator = BisectPaymentCalculator(balance = 600, annual_interest_rate = 0.02)
        result = calculator.initial_high
        self.assertIs(float, type(result))
        self.assertEqual(63.41, round(result, 2))

    def test_case_one(self):
        calculator = BisectPaymentCalculator(balance = 320000, annual_interest_rate = 0.2)
        self.assertEqual(
                29157.09,
                calculator.calculate_monthly_payment()
        )

    def test_case_two(self):
        calculator = BisectPaymentCalculator(balance = 999999, annual_interest_rate = 0.18)
        self.assertEqual(
                90325.03,
                calculator.calculate_monthly_payment()
        )

if __name__ == '__main__':
    unittest.main()
