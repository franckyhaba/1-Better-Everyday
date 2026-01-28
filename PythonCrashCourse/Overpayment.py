def calculate_overpayment(invoice_amount, amount_paid):
    if amount_paid > invoice_amount:
        return amount_paid - invoice_amount
    else:
        return 0


invoice = 10000.0

while True:
    try:
        payment = float(input("\nEnter the amount paid: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


overpayment = calculate_overpayment(invoice, payment)

if overpayment > 0:
    print(f"\nOverpayment detected: £{overpayment}")
else:
    print("\nNo overpayment detected.")
