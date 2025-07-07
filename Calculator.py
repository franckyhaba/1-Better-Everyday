# Simple Calculator Program
Msg = ("Welcome to franckys Calculator!")
print(Msg) 
print ()


firstNum= int(input ("Enter first number: "))
secondNum = int (input("Enter second number: "))
operator= input("Enter operator (+, -, *, /): ")


if operator == '+':
    result = (firstNum + secondNum)
elif operator == "-":
    result = (firstNum- secondNum)
elif operator == "*": 
    result = (firstNum * secondNum)
elif operator == "/":
    result = (firstNum / secondNum)
else: 
    result = "Invalid operator, please use +, -, *, or /"

print("The result is: ", result)

