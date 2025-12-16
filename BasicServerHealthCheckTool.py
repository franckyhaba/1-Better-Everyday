serversStatus =  {

"WEB01" : "UP",
"DBO01" :  "Down",
"ETH01"  : "UP",
"AIR01"   : "Down",
"FRA01"   :    "Down",
"BIC01"    : "UP"

}

while True: 
    info = input('\nPlease enter what servers to check: ')
    info = info.upper()
    ''''Can write the above code like or just put it at the end .upper()'''
    if info in serversStatus:
        print(f"\nThe server {info} has been located! ")
        break
    else:
        print(f"\nThe server {info} cant be located try again. ")

def healthCheck(verbose):
    
    serverCheck = input("\nDo want to check the server health? please enter 'Y\N'").upper()
    
    if  serverCheck == 'Y':
        print(f"The {info} health check came back {status}")

    
    else:
        print(f"The {info} health check wasn't preformed")
        
        
        
    for server, status in  serversStatus.item():
        print(f"The {server} health check came back {status}")
        


    healthCheck()