def multi(n):
    
    for i in range(1, n + 1):
        
        if i % 3 == 0 and i % 7 == 0:
            
            print('ThreeSeven') 
            
        elif i % 3 == 0 :
            print('Three')
            
        elif i % 7 == 0 :
            print('Seven')
            
        else: 
            print (i)

multi(15)