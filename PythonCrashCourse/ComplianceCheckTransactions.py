restrictedItems = ["TobaccoCorp", "CoalEnergy", "WeaponsLtd"]

restrictedItems = ["TobaccoCorp", "CoalEnergy", "WeaponsLtd"]

while True:
    msg = input("\nPlease enter the company you want to buy from: ")

    if msg in restrictedItems:
        print(f"\nCannot make purchase from {msg}. Try again.")
        continue

    print(f"\n{msg} is allowed. What is your offer?")
    msg3 = float(input("Enter offer: "))

    if msg3 > 10000:
        print(f"\nOffer of £{msg3} is too high — try again.")
        continue

    print(f"\nOffer of £{msg3} for {msg} has been accepted!")
    break

    
    
    
    
    