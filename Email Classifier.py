

def emailClassifier() :
    while True:
            email = str(input('Please input your email so we can classify it in system:"eg. info@Pyexll.com"....   '))
            print(email)
            if  "@" not in email or ".com" not in email:

             print(f'Your {email} is missing an "@".')
             continue
         
            else:
                
            
                if email == 'someone@gmail.com': 
                    print(f'Your {email} has been sorted in the personal email sections.')
                    
                elif email == 'junkuser@random.com':
                    print(f'Your {email} has been sorted in the junk email sections.')
                
                elif email == 'email1@company.com':
                    print(f'Your {email} has been sorted in the work email sections.')
                        
                    
                
         
emailClassifier()