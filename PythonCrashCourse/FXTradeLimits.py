intro= " \n ==== Welcome to the FX trading platform, all trades are made ! ===== "

currency = {
    "Swedish Krone": 12.51,
    "Euro": 1.14,
    "Dollars": 1.31
}


print(intro)
for name in currency :
    
    currencyTrade = input("\n Please select the currency you want to trade your pounds to:  ")
    
    currencyTrade = currencyTrade.title()
    
    if currencyTrade in currency:
        currencyTrade.title()
        print(f"\n The currency '{currencyTrade}' select can be traded!")
        break
    else:
        currencyTrade not in currency
        print(f"\nThe currency '{currencyTrade}' can't be traded try again! ")
        continue 
        
    
# currencyTrade = "\n Please select the currency you want to trade your pounds to:  "
# print(currencyTrade)

while True :
    
    trade = float(input("\n Enter FX trade size you want to make in £: "))

    maxT  = 5000001
    lowT = 1

    if trade > maxT:
        print(f"\n The max trade is 5,000,000 your trade of {trade} has surpassed the max try again!! ")
        continue
        
    elif  trade < lowT:
        print(f"\n The trade amount of {trade} is too low and can't be accepted try again!!")
        continue
    
    else: 
        print(f"\n The trade amount of {trade} has been accepted!!")
        print()
        break 
    
exRate = currency[currencyTrade]  
calcFX = trade * exRate

print(f"\n The Currency change was {currencyTrade}, and you changed '£{trade}' to {currencyTrade} {calcFX}.")

msg = input("Do you want make another trade? 'YES/NO': ")
msg = msg.title
print (msg)

if msg == 'YES':
    

