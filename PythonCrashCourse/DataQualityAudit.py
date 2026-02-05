invoices = [
    ("FP001", "BNP", 5000, "PAID"),
    ("FP002", "LVMH", -2500, "PAID"),
    ("FP003", "", 7000, "UNPAID"),
    ("FP004", "RNO", 0, "PAID"),
    ("FP005", "BAOC", 4000, "CLOSED")
]

def data_quality(invoices):
    invalid = {}

    for ref, name, amount, status in invoices:
        issues = []

        if name == "":
            issues.append("Missing supplier name")

        if amount <= 0:
            issues.append("Invalid amount")

        if status not in ("PAID", "UNPAID"):
            issues.append("Invalid status")

        if issues:
            invalid[ref] = issues

    return invalid


    
    
while True:
    intro = input(
        "\nDo you want to check data quality? Enter 'Y' or 'N': "
    ).upper()

    if intro == 'Y':
        print("\nChecking data quality.....")

        invalid_invoices = data_quality(invoices)

        if invalid_invoices:
            for ref, issues in invalid_invoices.items():
                print(f"\nInvoice {ref}:")
                for issue in issues:
                    print(f" - {issue}")
        else:
            print("\nNo data quality issues found.")

    elif intro == 'N':
        print("\nExiting, have a good day!")
        break
    else:
        print("\nInvalid input. Please enter Y or N.")
