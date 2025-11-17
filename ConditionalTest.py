# Goal of this program is to understand if statement etc, and also understand boolean term


Users =  ["francky", "mathew", "raoul", "sean", "jessica", "paddy", "marcie"]

while True :
    newUser = input("\n Please enter user name: ")
    
    if  newUser not in Users:
        print(f"\n{newUser} is not a user, user name has been accepted. ")
        Users.append(newUser)
        print(Users)
        break
        print(Users)
    else:
        newUser in Users
        print(f"\n{newUser} user name is taken try again. ")
        

# else :
#     newUser in Users  
#     print(f"\n {newUser} is one of our users.")