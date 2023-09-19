a = input("Enter first number: ")
b = input("Enter second number: ")

# Convert the user inputs to integers
a = int(a)
b = int(b)

c = input("What would you like to perform? ")

if c == "addition":
    result = a + b
    print("The sum is:", result)
elif c == "subtraction":
    result = a - b
    print("The difference is:", result)
elif c == "multiplication":
    result = a * b
    print("The product is:", result)
elif c == "division":
    if b == 0:
        print("Cannot divide by zero.")
    else:
        result = a / b
        print("The quotient is:", result)
else:
    print("Invalid operation. Please choose from 'addition', 'subtraction', 'multiplication', or 'division'.")
