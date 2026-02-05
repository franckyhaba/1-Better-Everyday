

payments = [
    ("BNP", 5000),
    ("LVMH", 2500),
    ("BNP", 7000),
    ("RNO", 16000),
    ("BNP", 3000),
    ("BAOC", 4000)
]
flaggedPaymentAmount: "10000"


def riskCheck(payments, flaggedPaymentAmount):
    
        
    invalid = {}
    
    for name, amount in payments:
        flaggedPayment = []
        unflaggedPayment = []
        totalSpend = []
        if name in payments == name:
            + amount
            totalSpend.append
            
        if payments >= flaggedPaymentAmount :
            flaggedPayment.append('flagged')
            print(f"This payment of '{flaggedPayment}' has been flagged")
        else:
            unFlaggedPayment = []
            payments <= flaggedPaymentAmount
            unflaggedPayment.append('not flagged')
                
            print(f"This payment of '{unFlaggedPayment}' are all alined ")
            
        if flaggedPayment:
            invalid[name]=flaggedPayment 
    print(f"The total payments of companies is : {payments}")


