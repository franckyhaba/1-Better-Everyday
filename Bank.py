msg= 'welcome to franckys Bank!'
print(msg)
print()
balance = 1000
while True: 
        try:
            
            menu = int(input("Enter 1 to Check Balance, 2 to deposit, 3 to withdraw, 4 to exit: "))
        except ValueError:
            print("Invalid input, please enter a number.")  
            print()
            continue  # Restart the loop if input is invalid
            
        if menu == 1:
            print("Your current balance is: $1000")
        elif menu == 2:
            while True:
                try:
                    deposit = int(input("Enter amount to deposit: "))
                    if deposit <= 0:
                        print("Deposit amount must be greater than zero.")
                        continue 
                    balance += deposit
                    print(f"You have deposited ${deposit}. Your new balance is: ${balance}")
                    break # Exit loop if input is valid
                except ValueError:
                    print("Invalid input, please enter a number.")
                    print()

        elif menu == 3:
            withdraw = int(input("Enter amount to withdraw: "))
            if withdraw <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif withdraw > 1000:
                print("Insufficient funds. You cannot withdraw more than your current balance.")
            else : withdraw <= balance
            balance -=withdraw 
            print(f"You have withdrawn ${withdraw}. Your new balance is: ${balance}")
        elif menu == 4:
            print("Thank you for using franckys Bank!")
            print("Goodbye!")
        elif menu < 1 or menu > 4:
            print("Invalid option. Please enter 1, 2, 3, or 4.")
        print()