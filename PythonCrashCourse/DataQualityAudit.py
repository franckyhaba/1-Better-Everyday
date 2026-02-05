payments = [
    ("BNP", 5000),
    ("LVMH", 2500),
    ("BNP", 7000),
    ("RNO", 16000),
    ("BNP", 3000),
    ("BAOC", 4000)
]

FLAGGED_PAYMENT_AMOUNT = 10000


def risk_check(payments, flagged_payment_amount):
    total_spend = {}
    flagged_suppliers = {}

    for supplier, amount in payments:
        if supplier in total_spend:
            total_spend[supplier] += amount
        else:
            total_spend[supplier] = amount

    for supplier, total in total_spend.items():
        if total > flagged_payment_amount:
            flagged_suppliers[supplier] = total

    return flagged_suppliers


flagged = risk_check(payments, FLAGGED_PAYMENT_AMOUNT)

if flagged:
    print("Flagged suppliers (exceed risk threshold):")
    for supplier, total in flagged.items():
        print(f"{supplier}: £{total}")
else:
    print("No suppliers exceed the risk threshold.")

