"""
Function: checkPasswordStrength()

This function prompts the user to enter a password and keeps asking until the password meets the following criteria:

- At least 8 characters long
- Contains at least one number
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one special character (e.g. !@#$%^&*())

If the password doesn't meet the criteria, the program will print what the password is missing.

Once a valid password is entered, it prints "Password accepted." and exits the loop.
"""
import string 
passRules = """- At least 8 characters long 
- Contains at least one number
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one special character (e.g. !@#$%^&*()))
"""
print(passRules)

reqPass = input('Please input password password must follow the rules listed above: ')

def checkPasswordStrength(reqPass) :
   while True:  
                
    hasNum = any(char.isdigit() for char in reqPass)
    hasUpper= any(char.isupper() for char in reqPass)         
    hasLower = any(char.islower() for char in reqPass)
    hasSpecial = any(char in string.punctuation for char in reqPass)           
    longNum = len(reqPass)>= 8                     
                
    if hasNum and hasUpper and hasLower and hasSpecial and longNum:
        print("Password has been accepted ")
        break
     
    else: 
        print("Password is missing: ")
        if not hasNum: 
         print("- number ")    
         
        print("Password is missing: ")
        if not hasUpper: 
         print("- Upper case ")    
         
        print("Password is missing: ")
        if not hasLower: 
         print("- Lower Case")    
          
        print("Password is missing: ")
        if not hasSpecial: 
         print("- special character ")    
          
     
        if not longNum: 
         print("Password is not long enough")    
         
    
    
   