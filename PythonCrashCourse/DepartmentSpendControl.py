expenses = [
    ("IT", 3000),
    ("Marketing", 4000),
    ("IT", 5000),
    ("Finance", 2000),
    ("Marketing", 7000),
    ("IT", 4000)
]

maxSpend = 10000

def exccedSpend (name, amount):
    overSpend = {}
    totalSpend = {}
    for name, amount in expenses:
        if 