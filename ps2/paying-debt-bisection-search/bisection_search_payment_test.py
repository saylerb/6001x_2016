import unittest

from bisection_search_payment import BisectPaymentCalculator

class TestBisectPaymentCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = BisectPaymentCalculator(600, 0.02)

    def tearDown(self):
        self.calculator = None

    def test_it_has_attributes(self):
        self.assertEqual(600.0, self.calculator.initial_balance)
        self.assertEqual(0.02, self.calculator.annual_interest_rate)

    def test_it_generates_a_low_guess(self):
        result = self.calculator.initial_low()
        self.assertIs(float, type(result))
        self.assertEqual(50.0, result)

    def test_it_generates_a_high_guess(self):
        result = self.calculator.initial_high()
        self.assertIs(float, type(result))
        self.assertEqual(63.41, round(result, 2))

    def test_case_one(self):
        self.calculator.initial_balance = 320000
        self.calculator.annual_interest_rate = 0.2

        self.assertEqual(29157.09, self.calculator.calculate_monthly_payment())

    def test_case_two(self):
        self.calculator.initial_balance = 999999
        self.calculator.annual_interest_rate = 0.18

        self.assertEqual(90325.03, self.calculator.calculate_monthly_payment())

if __name__ == '__main__':
    unittest.main()
