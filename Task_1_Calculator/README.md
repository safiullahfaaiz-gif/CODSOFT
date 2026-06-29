# Simple Calculator Program

# Prompt user for input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Perform calculation
if choice == '1':
    result = num1 + num2
    operation = "+"
elif choice == '2':
    result = num1 - num2
    operation = "-"
elif choice == '3':
    result = num1 * num2
    operation = "*"
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        operation = "/"
    else:
        result = "Error! Division by zero."
        operation = "/"
else:
    result = "Invalid choice!"
    operation = "?"

# Display result
print(f"\nResult: {num1} {operation} {num2} = {result}")
