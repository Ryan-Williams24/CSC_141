# Add two numbers and handle ValueError
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    sum = int(num1) + int(num2)
    print(f"The sum is: {sum}")
except ValueError:
    print("Please enter valid numbers.")