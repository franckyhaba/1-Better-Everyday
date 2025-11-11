print("Welcome to your simple expense analyzer!\n")

monthlyLimits = (500,350,700,) #food, transport, events 

foodExpenses = []
transportExpenses = []
eventsExpenses = []

print("Please input your expense details: ")
foodExpenses.append(float(input('Money spend on food (£): ')))
transportExpenses.append(float(input('Money spend on transport (£): ')))
eventsExpenses.append(float(input('Money spend on events (£): ')))

# calc totals 

totalFood = sum(foodExpenses)
totalTransport = sum(transportExpenses)
totalEvents = sum(eventsExpenses)

# print the calc

print("\n==== Monthly Summary ====")
print(f'Food: £{totalFood}/{monthlyLimits[0]}')
print(f'Transport: £{totalTransport}/{monthlyLimits[1]}')
print(f'Events: £{totalEvents}/{monthlyLimits[2]}')

print ("\nBudget check: ")

for category, total, limit in zip(
        ["Food", "Transport", "Events"],
        [totalFood,totalTransport,totalEvents],
        monthlyLimits 
):
    if total > limit:
        print(f"Over budget on {category}! ")
    else:
         print(f"your spending is under control {category}! ")