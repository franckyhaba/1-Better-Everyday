serversStatus =  {

"Web01" : "UP",
"DBO01" :  "Down",
"ETH01"  : "UP",
"AIR01"   : "Down",
"FRA01"   :    "Down",
"BIC01"    : "UP"

}

while True: 
    info = input('Please enter what servers to check: ')
    info = info.upper()
    ''''Can write the above code like or just put it at the end .upper()'''
    if info in serversStatus:
        print(f"\nThe server {info} has been located! ")
        
    else:
        print(f"\nThe server {info} cant be located try again. ")

def healthCheck(verbose):

    if verbose == True:
        print ("detailed out")
    else:
        verbose == False
        print("minimal output")


    healthCheck()