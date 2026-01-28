def describePets( type, name):
    
    """" Display information on pets """
    print(f"\nI have a {type}.")
    print(f"\nmy {type} name is {name}.")
describePets('pig','jon')

''''you an added multi functions calls '''

describePets('fish','neo')

''''
KEYWORD ARGUMENTS

stops things like 
jon named pig

    |
    |
    |
    |
    V
    
'''


def describeCars( type, name):
    
    """" Display information on pets """
    print(f"\nI have a {type}.")
    print(f"\nmy {type} name is {name}.")
describeCars( type = 'astra',name ='jon')

'''
DEFAULT VALUES

you can added default value to the DEF 

like this def describeCars( type = 'CAR', name ):

'''