# Goal of this program is to understand if statement etc, and also understand boolean term


Users =  ["francky", "mathew", "raoul", "sean", "jessica", "paddy", "marcie"]

newUser = input("\n Please enter user name: ")

if  newUser not in Users:
        Msg = f"\n{newUser} is not a user, i predict it will be false"
        print(Msg) 

elif newUser in Users:  
        print(f"\n {newUser} is one of our users.")