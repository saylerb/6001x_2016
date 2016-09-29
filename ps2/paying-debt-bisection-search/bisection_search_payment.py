class BisectPaymentCalculator:
    def __init__(self, balance, annual_interest_rate):
        self.initial_balance = balance * 1.0
        self.annual_interest_rate = annual_interest_rate

    def initial_low(self):
        return self.initial_balance / 12.0

    def initial_high(self):
        return (self.initial_balance * (1 + self.annual_interest_rate) ** 12)/12

    def calculate_monthly_payment(self):

        monthly_interest_rate = self.annual_interest_rate / 12.0
        low = self.initial_low()
        high = self.initial_high()
        balance = self.initial_balance

        while high - low > 0.001:
            guess = (high + low)/2

            for month in range(1, 13):

                interest = (balance - guess) * monthly_interest_rate
                balance = balance - guess + interest

            if balance > 0:
                low = guess
                balance = self.initial_balance
            else:
                high = guess
                balance = self.initial_balance

        return round(guess, 2)
