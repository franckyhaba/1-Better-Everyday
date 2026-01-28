def calculate_overpayment(invoice_amount, amount_paid):
    if amount_paid > invoice_amount:
        return amount_paid - invoice_amount
    else:
        return 0


# Test example
invoice = 10000.0
payment = float(input("\n Enter the amount paid: "))

overpayment = calculate_overpayment(invoice, payment)

if overpayment > 0:
    print(f"\nOverpayment detected: £{overpayment}")
else:
    print("\nNo overpayment detected.")
