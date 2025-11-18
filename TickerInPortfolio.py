# list of tickers 
tickers = ["MC fp", "RI fp","BNP fp", "OR fp", "CA fp", "RNO fp"]

for ticker in tickers:
    addTicker = (input("Enter the ticker you want to the portfolio: "))
    addTicker == tickers 
    print ("This tickers is already in the portfolio try again! ")

    if  addTicker != tickers:
        print ("The ticker has been added to the portfolio! ")
        print(tickers)
        break 
            