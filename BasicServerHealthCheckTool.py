ServersStatus =  {

"Web01" : "UP",
"DBO1" :  "Down",
"ETH01"  : "UP",
"AIR01"   : "Down",
"FRA01 "   :    "Down",
"BIC01"    : "UP"

}

info = input('Please enter what servers to check: ')

def healthCheck(verbose):

    if verbose == True:
        print ("detailed out")
    else:
        verbose == False
        print("minimal output")


    healthCheck()