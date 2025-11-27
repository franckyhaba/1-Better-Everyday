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

"""
print (intro)

stage1 = input("")


investments = ["ETF EURO", "Tech fund", "US index", "Real estate","Crypto"]

returns = ["4.5%","-4.1%", "-1.33%", "7%","15%"]

performance = { 
               "best": ('Crypto', 15),
               "worst": ('Tech fund', -4.1),
               "AvergReturn": ('Real estate', 7),
               "aboveAverg": ['Crypto', "US index"],
               "belowAverg": ['ETF Euro','tech fund' ]
               
               
}

msg = input("/n ")
    
    
    
    

    
    
    
