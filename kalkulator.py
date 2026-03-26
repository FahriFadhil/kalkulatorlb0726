# Initial Commit

# 1. Ask the user for two numbers
# We use float() so the user can enter decimals (like 10.5)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 2. Ask the user for the operation
print("Select operation: +, -, *, /")
operation = input("Enter choice (+, -, *, /): ")

# 3. Perform the calculation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid input! Please choose a valid operator.")