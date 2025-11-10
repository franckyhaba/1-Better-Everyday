print("Welcome to your simple expense analyzer!\n")

MonthlyLimits = (500,350,500,) #food, transport, events 

foodExpenses = []
transportExpenses = []
eventsExpenses = []

print("Please input your expense details: ")

foodExpenses.append(float(input('Money spend on food (£): ')))
transportExpenses.append(float(input('Money spend on transport (£): ')))
eventsExpenses.append(float(input('Money spend on events (£): ')))