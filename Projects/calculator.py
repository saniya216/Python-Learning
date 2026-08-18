num1 = float(input("Enter first num:"))
num2 = float(input("Enter second num:"))

operator = input("Enter operator (+, -, *, / ) :")

if operator == "+":
    result = num1 + num2
    print("Result =", result)

elif operator == "-":
    result = num1 - num2
    print("Result =", result)

elif operator == "*":
    result = num1 * num2
    print("Result =", result)

elif operator == "/":
    result = num1 / num2
    print("Result =", result)

else:
    print("Operator not Valid")