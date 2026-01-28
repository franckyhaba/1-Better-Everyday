invoice =  float("10000")

intro = "\nThis system is to pay for your invoice."
print(intro)
payment = float(input("\nEnter the amount the amount you want to pay: "))
print (payment)

if payment == invoice:
    print (f"\nYour payment of ${payment} has covered all of the invoice")
    
elif payment > invoice:
    
    calOverPayment = invoice - payment 
    
    print (f"\nThe ${payment} of is an overpayment, you a due a return of  ${calOverPayment}")
    
else :
    payment < invoice
    CalUnderPayment = invoice - payment 
    
    print (f"\nThe ${payment} of is an underpayment, you still have an outstanding balance of ${CalUnderPayment}")
    