import math
import argparse


# Initialise parser
parser = argparse.ArgumentParser(description="The credit calculator")


# Add optional arguments
parser.add_argument("--type", choices=["annuity", "diff"], help='The type of payment')
parser.add_argument("--principal", type=int, default=0, help='The credit principal')
parser.add_argument("--payment", type=float, default=0.0, help='The annuity payment')
parser.add_argument("--periods", type=int, default=0, help=' Number of payments. '
                                                           'Usually, it’s the count of months.')
parser.add_argument("--interest", type=float, default=0.0, help='The annual interest rate')

# Parse the arguments
args = parser.parse_args()

_type_ = args.type
principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest

# Looking for incorrect parameters
if any([not all([_type_, _type_ in ["annuity", "diff"], interest > 0.0]),
        _type_ == "diff" and not all([principal > 0, periods > 0, payment == 0.0]),
        _type_ == "annuity" and not any([
                                        all([principal > 0, periods > 0, payment == 0.0]),
                                        all([principal > 0, payment > 0.0, periods == 0]),
                                        all([periods > 0, payment > 0.0, principal == 0])
                                        ])
        ]):

    print("Incorrect parameters.")

else:

    i = interest / (12 * 100)  # Calculate nominal (monthly) interest rate

    if _type_ == "annuity":

        # Credit principal calculations:
        if principal == 0:
            principal = math.floor(payment / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)))
            print(f"Your credit principal = {principal}!")

        # Annuity payment calculations:
        elif payment == 0:
            payment = math.ceil(principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
            print(f"Your annuity payment = {payment}!")

        # Periods calculations:
        elif periods == 0:
            periods = math.ceil(math.log((payment / (payment - i * principal)), 1 + i))
            years = periods // 12
            years = str(years) + ("year" if years == 1 else "years")
            months = math.floor((periods % 12) * 1)
            months = str(months) + ("month" if months == 1 else "months")

            if years == 0:
                count_of_months = f"You need {months} to repay this credit!"
            elif months == 0:
                count_of_months = f"You need {years} to repay this credit!"
            else:
                count_of_months = f"You need {years} and {months} to repay this credit!"

            print(count_of_months)

        overpayment = round(payment * periods - principal)

    # Differentiated payment calculations:
    elif _type_ == "diff":

        diff_payments = []

        for m in range(1, periods + 1):

            diff_payment = math.ceil((principal / periods) +
                                     i * (principal - (principal * (m - 1)) / periods))
            diff_payments.append(diff_payment)

            print(f" Month {m}: paid out {diff_payment}")

        overpayment = round(sum(diff_payments) - principal)

    print(f"\nOverpayment = {overpayment}")
