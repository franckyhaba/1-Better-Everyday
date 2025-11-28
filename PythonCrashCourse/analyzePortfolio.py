intro = """
=== Welcome to the portfolio analyse ===
\nThis app is to track portfolio information.
It helps you monitor investments!

\nselect the following number based on what information 
you want to see 
\n
1. Investment in portfolio 
2. Portfolio return in '%'
3. Portfolio Performance 
4. Add new Investment
5. Exit

"""
print (intro)

investments = [
    "ETF EURO",
    "Tech fund", 
    "US index", 
    "Real estate",
    "Crypto"
    ]

returns = ["4.5%","-4.1%", "-1.33%", "7%","15%"]

performance = { 

    "best": ('Crypto', 15),
    "worst": ('Tech fund', -4.1),
    "avergReturn": ('Real estate', 7),
    "aboveAverg": ['Crypto', "US index"],
    "belowAverg": ['ETF Euro','tech fund' ]
}



while True : 
    
    menu = {
        1: 'Investment in portfolio',
        2: "Portfolio return in '%'",
        3: 'Portfolio Performance', 
        4: 'Add new Investment',
        5: 'Exit'
}
      
        
        
        
    }
    introList = {
        1: "Investment in portfolio",
        2: "Portfolio return in '%'",
        3: "Portfolio Performance", 
        4: "Add new Investment",
        5: "Exit"
}
    
    stage1 = int(input("\n Please select a number from the list 1-4: "))
    
    
    if stage1 not in introList:
        print(f"\n {stage1} is not in the list try again!!! ")
        
        
    
        
    
    elif stage1 :
        stage1 == 1
        print('\n Investment in portfolio was selected' )
        print(f'\nThe investment in your portfolio are {investments}')
        
    elif stage1 :
        stage1 == 2
        print('\n Portfolio return was selected' )
        print(f'\nThe investment in your portfolio are {investments}')
    
    


    
    
    

    
    
    
