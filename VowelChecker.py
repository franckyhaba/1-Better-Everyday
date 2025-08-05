msg = input(("Enter a word so we can find the vowel:  "))


def checkVowel (msg):
    
    vowels= {
            'a','e','i','o','u' 
            }
    
    while True :
        if msg == 'a,e,i,o,u':
            
            print ('You got a vowel in the {msg}')
            break 
        
        else :
            print('The is no vowel in the word {msg}') 
        continue
checkVowel(msg)
            
            
            