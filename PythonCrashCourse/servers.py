# Write a Python script that:
# Reads a list of server names from a file called servers.txt.
# Pings each server once.
# Records the result (UP or DOWN) into a log file named healthcheck.log.
# Includes a function to format the log output.
# Uses a loop, lists, functions, and error handling.
# Prints a short summary at the end showing:
# total servers checked
# how many were up
# how many were down



serversName = {
    'Art':  'Up', 
    'Aws': 'Down',
    'Hubspot': 'Down',
    'Meta': 'Up',
    'Microsoft': 'Up'  
}

healthCheck = []

while True:
    questions = input("\nPlease enter the server you want to check?: ").strip().title()
        
    if questions in serversName:
        print(f"\nFound server {questions} in list")
        continue 
    else:  
        print(f"\n Server {questions} cannot be found, please try again")


    
    
    
    def healthcheck():
        servers = input("\nPlease input the server name that you want to see the health check: ")
        if servers in serversName: 
            print(f"\n {servers} has had a health check preformed on it")
            continue
        else: 
            print(f"\n {servers} has not had a health check! ")
            
        for servers, status in serversName.items(): 
            print(f"The {servers} health check came back {status}")
    healthcheck()


