
def checkVowel ():
    
    vowels= { 'a','e','i','o','u' }
    
    while True: 
        msg = input(("Enter a word so we can find the vowel:  "))
        found = False

        for char in msg.lower(): # Check each letter
         
            if char in vowels: 
                print(f"✅ You got a vowel: '{char}' is in '{msg}'")
                found = True
                break
           
            
        if found: 
                
               break
        else:
            print(f"❌ There is no vowel in the word '{msg}'") 
            print ()
        
checkVowel()
            
            
            