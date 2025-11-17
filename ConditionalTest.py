# Goal of this program is to understand if statement etc, and also understand boolean term


Users =  ["francky", "mathew", "raoul", "sean", "jessica", "paddy", "marcie"]

user = "Axcent"

if  user not in Users:
        Msg = f"\n{user} is not a user, i predict it will be false"
        print(Msg) 

elif user in Users:  
        print(f"\n {user} is one of our users.")