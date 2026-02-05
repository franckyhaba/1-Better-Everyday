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
        if name in totalSpend:
            totalSpend[name] += amount
        else:
            totalSpend[name] = amount
    
            

    for name, total in totalSpend.items():
        if total > maxSpend:
            overSpend[name] = total
    return overSpend

runFun = exccedSpend (expenses, maxSpend)

if runFun:
    print("Flagged departments (exceed budget threshold):")
    for name, amount in runFun.items():
        print(f"{name}: £{amount}")
else:
    print("No suppliers exceed the risk threshold.")