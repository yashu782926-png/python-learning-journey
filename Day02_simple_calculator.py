num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator == "*":
    result = num1 * num2
    print("Result:", result)
elif operator == "/":
    result = num1 / num2
    print("Result:", result)
else:
    print("Invalid operator. Please use +, -, *, or /.")
    