invoices = {
    "BNP FP": 5000,
    "LVMH FP": 2500,
    "MC FP": 70000,
    "RNO FP": 16000,
    "BAOC FP":4000,
    "BNP FP": 5000  
}



def detectDuplicatePayments(invoice, payments):
    
    if invoice:
        return 
    else:
        print("Zero duplicates can be found")
        

while True: 
    intro = str(input("\nDo you want to check for Duplicates in Data if yes enter 'y' else 'N' to exit: ")).uppper
    
    if intro:
        intro == "Y"
        print("\nLooking for duplicates.....")
    
    elif intro:
        intro == "N"
        print("\n Exiting, have a good day!")
        break