class BisectPaymentCalculator:
    def __init__(self, balance, annual_interest_rate):
        self.initial_balance = balance * 1.0
        self.annual_interest_rate = annual_interest_rate
        self.monthly_interest_rate = annual_interest_rate/12.0
        self.initial_low = balance / 12
        self.initial_high = (balance * (1 + annual_interest_rate) ** 12)/12

    def calculate_monthly_payment(self):

        low = self.initial_low
        high = self.initial_high
        balance = self.initial_balance

        while high - low > 0.001:
            guess = (high + low)/2

            for month in range(1, 13):

                interest = (balance - guess) * self.monthly_interest_rate
                balance = balance - guess + interest

            if balance > 0:
                low = guess
                balance = self.initial_balance
            else:
                high = guess
                balance = self.initial_balance

        return round(guess, 2)
