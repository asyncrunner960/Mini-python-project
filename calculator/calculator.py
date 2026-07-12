# Simple command-line calculator
# Performs basic arithmetic operations

print("Welcome to the Python Calculator!")
print("Enter two numbers and an operation.")
print("Operations: +, -, *, /, //, %")
print("Type 'quit' as the operation to exit.")

while True:
    try:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        operation = input("Enter operation: ")

        if operation == "quit":
            print("Goodbye!")
            break

        if operation == "/" and second_num == 0:
            print("Error: Division by zero is not allowed.")
        elif operation == "+":
            print(f"Result: {first_num + second_num}")
        elif operation == "-":
            print(f"Result: {first_num - second_num}")
        elif operation == "*":
            print(f"Result: {first_num * second_num}")
        elif operation == "/":
            print(f"Result: {first_num / second_num}")
        elif operation == "//":
            # Floor division, e.g., 7 // 2 = 3
            print(f"Result: {first_num // second_num}")
        elif operation == "%":
            # Modulo, remainder of division
            print(f"Result: {first_num % second_num}")
        else:
            print("Invalid operation. Please use +, -, *, /, //, %.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")