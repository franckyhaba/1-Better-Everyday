

def emailClassifier() :
    while True:
            email = str(input('Please input your email so we can classify it in system:"eg. info@Pyexll.com"....   '))
            print(email)
            if  "@" not in email or ".com" not in email:

                print(f'Your {email} is missing an "@".')
                continue
            
            else:
                if email.endswith('@gmail.com'): 
                    print(f'Your {email} has been sorted in the personal email sections.')
                    
                elif email.endswith('@random.com'):
                    print(f'Your {email} has been sorted in the junk email sections.')
                
                elif email.endswith('@company.com'):
                    print(f'Your {email} has been sorted in the work email sections.')
                    
                else:
                    print(f'Your {email} does not match any known category.') 
                break
emailClassifier()