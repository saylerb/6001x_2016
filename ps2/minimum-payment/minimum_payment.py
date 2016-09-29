def balance_after_12_minimum_payments(balance, annual_interest_rate, monthly_payment_rate):
    """returns the remaining balance of a loan after 12 miniumum payments"""

    total_paid = 0
    monthly_interest_rate = annual_interest_rate / 12.0

    for month in range(1, 13):
        minimum_monthly_payment = monthly_payment_rate * balance
        monthly_unpaid_balance = balance - minimum_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance + \
            (monthly_interest_rate * monthly_unpaid_balance)

        balance = updated_balance_each_month
        total_paid += minimum_monthly_payment
        if month == 12:
            return {'Remaining balance': round(balance, 2)}
