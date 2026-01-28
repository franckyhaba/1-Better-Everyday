invoices = [
    ("BNP FP", 5000),
    ("LVMH FP", 2500),
    ("MC FP", 70000),
    ("RNO FP", 16000),
    ("BAOC FP", 4000),
    ("BNP FP", 5000)  # duplicate
]

def detect_duplicate_payments(invoices):
    seen = {}
    duplicates = {}

    for ref, amount in invoices:
        if ref in seen:
            duplicates[ref] = duplicates.get(ref, amount) + amount
        else:
            seen[ref] = amount

    return duplicates



while True:
    intro = input(
        "\nDo you want to check for duplicates in data? Enter 'Y' or 'N': "
    ).upper()

    if intro == "Y":
        print("\nLooking for duplicates.....")

        duplicate_invoices = detect_duplicate_payments(invoices)

        if duplicate_invoices:
            for ref, total in duplicate_invoices.items():
                print(f"Duplicate detected: {ref} | Total Paid: £{total}")
        else:
            print("No duplicate payments found.")

    elif intro == "N":
        print("\nExiting, have a good day!")
        break
    else:
        print("Invalid input. Please enter Y or N.")
