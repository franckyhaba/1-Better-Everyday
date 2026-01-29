invoices = [
    ("FP001", "BNP", 5000, "PAID"),
    ("FP002", "LVMH", -2500, "PAID"),
    ("FP003", "", 7000, "UNPAID"),
    ("FP004", "RNO", 0, "PAID"),
    ("FP005", "BAOC", 4000, "CLOSED")
]

def dataQuality(invoices):
    paid = {}
    unpaid = {}
    invalid = {}
    
    for ref, amount, status, in invoices:
        if ref in invalid:
            invalid[ref] = invalid.get(ref, amount) + amount
        else:
            paid[ref] = amount
            unpaid[ref] = amount

    return invalid

    
    
    while True:
        
    
            