def LogLvl ():
    
    while True :
        
        try:
            Keyword = str(input("Enter log level: " )).upper()
            print (Keyword)
        
        except ValueError: 
            print('Please enter a Log level!')
            continue 
        
        for Error in Keyword:
            print(f'{Keyword} has been logged a error')
            
        if Keyword == "Warning":
            print(f'{Keyword} has been logged a Warning')
            
        elif Keyword == "info": 
            print(f'{Keyword} has been logged a info')
        else:
            print(f'{Keyword} No key word can be found')

LogLvl()