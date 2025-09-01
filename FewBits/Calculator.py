# Simple Calculator Program
Msg = ("Welcome to franckys Calculator!")
print(Msg) 
print ()

while True:
    try:  
        firstNum= int(input ("Enter first number: "))
        break # Exit loop if input is valid
    except ValueError:
        print("")
        print("Invalid input, please enter a number.")  
        print("")
while True:
    try:  
        secondNum = int (input("Enter second number: "))
        break # Exit loop if input is valid
    except ValueError:
        print("Invalid input, please enter a number.") 

operator= input("Enter operator (+, -, *, /): ")
print("")

if operator == '+': 
    result = (firstNum + secondNum)
elif operator == "-":
    result = (firstNum- secondNum)
elif operator == "*": 
    result = (firstNum * secondNum)
elif operator == "/":
    result = (firstNum / secondNum)
else: 
    print("")
    result = "Invalid operator, please use +, -, *, or /"

print("The result is: ", result)
# End of Calculator.py
print("")
print("Thank you for using franckys Calculator!")
print("")
print("Goodbye!")
print()
# End of program
