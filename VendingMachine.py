msg = "Welcome to Franckys Vending Machine, select what you would like:"
print(msg)
print()  # This creates a blank line for better spacing

balance = 5.00

while True:
    try:
        option = int(input("1. Water, 2. KitKat, 3. Coke, 4. Exit: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.\n")
        continue

    if option == 1:
        price = 2.00
        print(f"You have selected Water, and it costs £{price:.2f}\n")
        balance -= price 
        print (balance) 
    elif option == 2:
        price = 1.50
        print(f"You have selected KitKat, and it costs £{price:.2f}\n")
        balance -= price 
        print (balance) 
    elif option == 3:
        price = 2.50
        print(f"You have selected Coke, and it costs £{price:.2f}\n")
        balance -= price 
        print (balance) 
        
    elif option == 4:
        print("Thank you for using Franckys Vending Machine. Have a good day!\n")
        break

    else:
        print("Invalid option. Please select a number between 1 and 4.\n")
