monthlyExpenses = { 
                  'Rent': 500,
                  'Food': 60,
                  'Transport': 120,
                  'Fun': 80
                  }

instructions= ('category available "Rent", "Food", "Transport", "Entertainment"')
print(instructions)

for monthlyExpense in monthlyExpenses :
    chooseCat = input('\n Please choose from the category available "Rent", "Food", "Transport", "Entertainment": ')
    chooseCat.title()

    if chooseCat in monthlyExpenses: 
    
     msg = input(f"\n The category you have selected is {chooseCat}, PLease enter the amount spent this month:  ")
     print (msg)