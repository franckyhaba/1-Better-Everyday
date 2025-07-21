

def emailClassifier() :
    while True:
        try :
            email = str(input('Please input your email so we can classify it in system:"eg. info@Pyexll.com"....   '))
            print(email)
        except ValueError:
            print(f'Your {email} is missing an "@".')
            continue
            
            #for 'email1@company.com' in email :
                #print(f'Your {email} has been sorted in the work email sections.')
                
            if email == 'someone@gmail.com': 
                print(f'Your {email} has been sorted in the personal email sections.')
                
            elif email == 'junkuser@random.com':
                print(f'Your {email} has been sorted in the junk email sections.')
            
            elif email == 'email1@company.com':
                print(f'Your {email} has been sorted in the work email sections.')
                    
                
                
         
emailClassifier()