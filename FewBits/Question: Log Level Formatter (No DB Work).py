def LogLvl ():
    
    while True :
        
        try:
            Keyword = input("Enter log level: " ).upper()
            print (f'User entered {Keyword}')
        
        except ValueError: 
            print('Please enter a Log level!')
            continue 
        
        if  Keyword == "Error":
            print(f'{Keyword} has been logged a error')
            
        elif Keyword == "Warning":
            print(f'{Keyword} has been logged a Warning')
            
        elif Keyword == "info": 
            print(f'{Keyword} has been logged a info')
        else:
            print(f'{Keyword} No key word can be found')    
        break 

LogLvl()