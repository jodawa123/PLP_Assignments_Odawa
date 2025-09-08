# Get two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Get the operation
operation = input("Enter operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

# Show the result
print( num1, operation, num2,"=" ,result )

 