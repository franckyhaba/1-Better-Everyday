msg = "Welcome to Franckys Vending Machine, select what you would like:"
print(msg)
print()  # This creates a blank line for better spacing

balance = 5.00

while True:
    try:
        option = int(input("1. Water (£2.00), 2. KitKat (£1.50), 3. Coke (£2.50), 4. Exit: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.\n")
        continue

    if option == 1:
        item = "Water"
        price = 2.00
    elif option == 2:
        item = "KitKat"
        price = 1.50
    elif option == 3:
        item = "Coke"
        price = 2.50
    elif option == 4:
        print("Thank you for using Franckys Vending Machine. Have a good day!\n")
        break
    else:
        print("Invalid option. Please select a number between 1 and 4.\n")
        continue

    # ✅ Check balance BEFORE subtracting
    if balance < price:
        print("Insufficient funds. You don't have enough money for this item.\n")
        continue

    # ✅ Process purchase
    balance -= price
    print(f"You purchased {item} for £{price:.2f}. Remaining balance: £{balance:.2f}\n")

    # ✅ End if balance hits zero
    if balance <= 0:
        print("Your balance is £0.00. No more purchases can be made.\n")
        break
