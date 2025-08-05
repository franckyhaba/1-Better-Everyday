'''Asks the user to input a username.
Keeps asking until the username meets the following rules:
Must be at least 6 characters long.
Must start with a letter.
Must only contain letters, numbers, or underscores.
Must not contain any spaces.
If the username doesn't meet the criteria, print what it’s missing.

Once a valid username is entered, print "Username accepted." and exit the loop.
'''
import string 
msg = ( '''Asks the user to input a username.
Keeps asking until the username meets the following rules:
Must be at least 6 characters long.
Must start with a letter.
Must only contain letters, numbers, or underscores.
Must not contain any spaces.
If the username doesn't meet the criteria, print what it’s missing.''')
print(msg)
print()

userName = input('Please input username: ')

def checkUsernameValidity(userName):
    
    while True:
        longerSix = len(userName) >= 6 
        hasFirstLetter = userName and userName[0].isalpha()
        hasOnlyValidChars = all(char.isalnum() or char == '_' for char in userName)
        hasSpace = any(char .isspace() for char in userName)
        
        if longerSix and hasFirstLetter and hasOnlyValidChars and not hasSpace:
            print()
            print(f'{userName} has been been accepted ✅')
            break 
        else:
            
            if not longerSix:
                print (f'{userName }is not longer then 6 characters.')
             
            if not hasFirstLetter: 
                print (f'{userName } does not begin with a letter.')
            
            if not hasOnlyValidChars: 
                print (f'{userName }has no special characters.')
            
            if not hasSpace: 
                print (f'{userName } has a space please get rid of it.')
                
           
            print()
            userName = input('Please follow the rules when picking a username: ')  
             
    
checkUsernameValidity(userName)