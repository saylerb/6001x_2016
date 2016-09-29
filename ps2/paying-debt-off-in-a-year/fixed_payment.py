def calculate_monthly_payment(balance, annual_interest_rate):

    unpaid_balance = balance

    total_paid = 0
    monthly_payment = 0
    monthly_interest_rate = annual_interest_rate / 12.0

    while unpaid_balance >= 0:

        monthly_payment += 10
        unpaid_balance = balance

        for month in range(1, 13):
            unpaid_balance = unpaid_balance - monthly_payment
            total_paid += monthly_payment
            # compound the interest:
            unpaid_balance = unpaid_balance + (monthly_interest_rate * unpaid_balance)

            print("Month:", month)
            print("Payment:", monthly_payment)
            print("Remaining balance:", round(unpaid_balance,2))


    print("The optimal monthly payment is:", monthly_payment)
    return  {'Lowest payment': monthly_payment}
