import math

print("----Function Calculator----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    def add(a, b):
        return a + b

    result = add(a, b)
    print("The sum of " + str(a) + " and " + str(b) + " is: " + str(result))
elif choice == 2:
    def subtract(a, b):
        return a - b

    result = subtract(a, b)
    print("The difference of " + str(a) + " and " + str(b) + " is: " + str(result))
elif choice == 3:
    def multiply(a, b):
        return a * b

    result = multiply(a, b)
    print("The product of " + str(a) + " and " + str(b) + " is: " + str(result))
elif choice == 4:
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."

    result = divide(a, b)
    print("The quotient of " + str(a) + " and " + str(b) + " is: " + str(result))
    
print("Thank you for using the Function Calculator!")
