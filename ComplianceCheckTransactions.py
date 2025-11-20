restrictedItems = ["TobaccoCorp", "CoalEnergy", "WeaponsLtd"]

for company in restrictedItems:
    msg = input("\n Please enter the company you want to buy from: ")
    print (msg)

    if msg in restrictedItems:
        msg1 = (f"\n Can not make purchase from {msg} as it is a restricted item, try again")
        print(msg1)

    elif msg not in restrictedItems:
        msg2 = (f"\n {msg} is not in the restricted items what is your offer" )
        print(msg2)
        msg3 = float(input(f"\n Please enter offer: "))


    # The line `print(f"Your offer of {msg3}, has been flagged try again ")` is printing a message to
    # inform the user that their offer has been flagged for being too high. This message is displayed when
    # the user enters an offer that is greater than 10001. It prompts the user to try again with a
    # different offer within the acceptable range.
    if msg3 > 10000:
        print(f"\nYour offer of £{msg3} has been flagged — try again.")
         
        msg3 = float(input(f"\n Please enter offer: "))
        print(msg3)
        continue

    # Case 4: Offer is acceptable → break loop
        print(f"\nOffer of £{msg3} for {msg} has been accepted!")
        break
    
    
    
    
    
    # elif msg3 > 10001 : 
    #     print(f"Your offer of {msg3}, has been flagged try again ")

    # elif msg3 <= 10000: 
    #     print (f"Offer of {msg3} has been accepted")
    #     break 