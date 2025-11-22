intro= " ==== Welcome to the FX trading platform, all trades are made ! ===== "

currency = {
    "Swedish Krone",
    "Euro",
    "Dollars"
}


print(intro)
for currencys in currency.item(): 
    
    currencyTrade = "\n Please select the currency you want to trade your pounds to:  "
    print(currencyTrade)
    
    if currencyTrade in currency:
        print(f"The currency {currencyTrade} select can be traded!")
        break
    else:
        currencyTrade not in currency
        print(f"The currency {currencyTrade} can't be traded try again! ")
        continue 
        
    
# currencyTrade = "\n Please select the currency you want to trade your pounds to:  "
# print(currencyTrade)

while True :
    trade = float(input("\n Enter FX trade size you want to make in £ "))
    
    