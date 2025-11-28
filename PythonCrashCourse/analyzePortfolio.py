intro = """
=== Welcome to the portfolio analyse ===
\nThis app is to track portfolio information.
It helps you monitor investments!

\nSelect the following number based on what information 
you want to see 
"""
print (intro)

investments = [
    "ETF EURO",
    "Tech fund", 
    "US index", 
    "Real estate",
    "Crypto"
    ]

returns = {
    
    "ETF EURO": 4.5,
    "Tech fund": -4.1, 
    "US index": -1.33, 
    "Real estate": 7,
    "Crypto": 15
}

performance = { 

    "best": ('Crypto', 15),
    "worst": ('Tech fund', -4.1),
    "avergReturn": ('Real estate', 7),
    "aboveAverg": ['Crypto', "US index"],
    "belowAverg": ['ETF Euro','tech fund' ]
}
menu = {
            1: 'Investment in portfolio',
            2: "Portfolio return in '%'",
            3: 'Portfolio Performance', 
            4: 'Add new Investment',
            5: 'Exit'
} 


while True : 
    #show menu 
    for number, value in menu.items():
        print(f"{number}. {value}")
        
    stage1 = int(input("\n Please select a number from the list 1-5: "))
    
    #invalid options
    if stage1 not in menu:
        print(f"\n{stage1} is not in the list try again!!! ")
        continue 
    
    print(f"\nYou selected: {menu[stage1]}\n")
    
        
    if stage1 == 5:
        
        print("Exiting program... ")
        break 
    
    if stage1 == 1:
        print(f"\nHere are the current investment in your portfolio: {investments} \n")
        
    elif stage1 == 2:
        print(f"\nHere is the portfolio return and investments: \n{returns}")
    
    elif stage1 == 3:
        print(f"\nHere is the portfolio performance: {performance}")
    
    elif stage1 == 4:
        newInvestment = (input(f"\nAdd new investment: ")).tittle()
        investments.append(newInvestment) 
        print(f"\nNew investment '{newInvestment}' was added to the investments list. ")
        print(f"\n{investments}\n")
        
    
    # elif stage1 :
    #     stage1 == 1
    #     print('\n Investment in portfolio was selected' )
    #     print(f'\nThe investment in your portfolio are {investments}')
        
    # elif stage1 :
    #     stage1 == 2
    #     print('\n Portfolio return was selected' )
    #     print(f'\nThe investment in your portfolio are {investments}')
    
    


    
    
    

    
    
    
