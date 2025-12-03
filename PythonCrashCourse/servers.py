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
    'Art':  'up', 
    'Aws': 'Down',
    'Hubspot': 'Down',
    'Meta': 'up',
    'Microsoft': 'up:'
}

healthCheck = []

while True:
    questions = input("\nPlease enter the server you want to check?: ")
    questions = questions.title()
    
    if questions in serversName:
        print(f"\nFound server {questions} in list")
        break
    else:
        print(f"Server {questions} cannot be found, please try again")


    
    
    
        