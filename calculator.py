operator = input("Enter the arithmetic operator (+, -, *, /): ")
num1 = float(input("Enter the number 1: "))
num2 = float(input("Enter the number 2: "))
if operator == '+':
    addition = num1 + num2
    print(f"The sum of the the numbers you entered is {addition}")
elif operator == '-':
    difference = num1 - num2
    print(f"The difference between the numbers you entered is {difference}")
elif operator == '*':
    product = num1 * num2
    print(f"The product of the numbers you entered is {product}")
elif operator == '/':
    division = num1 / num2
    print(f"The result of dividing  the numbers you entered is {division}")
else:
    print("You entered invalid operator")