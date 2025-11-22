intro= " ==== Welcome to the FX trading platform, all trades are made ! ===== "

currency = {
    "Swedish Krone": .08,
    "Euro": .89,
    "Dollars": .76
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
    
    if trade > 5000001:
        print(f"\n The max trade is 5,000,000 your trade of {trade} has surpassed the max try again!! ")
        
    