monthlyExpenses = { 
                  'Rent': 500,
                  'Food': 60,
                  'Transport': 120,
                  'Fun': 80
                  }

instructions= ('category available "Rent", "Food", "Transport", "Entertainment"')
print(instructions)

for name, expense in monthlyExpenses.items():
    chooseCat= input('\n Please choose from the category available "Rent", "Food", "Transport", "Entertainment": ')
    chooseCat= chooseCat.title()

    if chooseCat in monthlyExpenses: 
    
     msg = float(input(f"\n The category you have selected is {chooseCat}, Please enter the amount spent this month:  "))
     print (msg)
     if msg <= sum(monthlyExpenses): 
         print("Your expenses fit with in the budget")
         break
     elif msg > chooseCat:
        print("You have went over the Budget!!!")
        