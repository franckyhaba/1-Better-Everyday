invoice =  "10000"

intro = "\nThis system is to pay for your invoice."
print(intro)
payment = float(input("\nEnter the amount the amount you want to pay: "))
print (payment)

if payment == invoice:
    print ("Your payment of {payment} has paid of the invoice")
    
