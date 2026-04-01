# simple Calculator
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
# Addition
result = num1+num2
print("Addition:", result)
# Subtraction
result = num1-num2
print("Subtraction:", result)
# multiplication
result = num1*num2
print("Multiplication:", result)
# Division
if num2 != 0:
    result = num1 / num2
    print("Division:", result)
else:
    print("Division: Cannot divide by Zero")
