payments = [
    ("BNP", 5000),
    ("LVMH", 2500),
    ("BNP", 7000),
    ("RNO", 16000),
    ("BNP", 3000),
    ("BAOC", 4000)
]
flaggedPaymentAmount: "10000"
def riskCheck(payments):
    
    for name, amount in payments:
        invalid = {}
    
    if payments >= flaggedPaymentAmount :
        flaggedPayment = []
        unflaggedPayment = []
        flaggedPayment.append('flagged')
        print(f"This payment of '{flaggedPayment}' has been flagged")
    else:
        unFlaggedPayment = []
        payments <= flaggedPaymentAmount
        unflaggedPayment.append('not flagged')
            
        print(f"This payment of '{unFlaggedPayment}' are all alined ")
        
    if flaggedPayment:
        invalid[name]=flaggedPayment 




# def calculate_overpayment(invoice_amount, amount_paid):
#     if amount_paid > invoice_amount:
#         return amount_paid - invoice_amount
#     else:
#         return 0