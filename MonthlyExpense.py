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
     if msg <= monthlyExpenses[chooseCat]: 
         print(f"\n Your {chooseCat} expenses of £{msg} fit with in the budget")
         print ("\n Thanks your expense has been stored!!")
         break
     elif msg > monthlyExpenses[chooseCat]:
         print(f"\n Your {chooseCat} expenses of £{msg} doesn't fit in the budget, try again!")
        