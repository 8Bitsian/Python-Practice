# Basic Calculator: User provides two numbers and selects an operation (+, -, *, **, /, %)

# Define functions for each arithmetic operation
def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def exponent(x, y):
  return x ** y
def division(x, y):
  # Validate if y is 0
  if y == 0:
    return "ERROR: Cannot Divide by 0"
  return x / y
def modulus(x, y):
  # Validate if y is 0
  if y == 0:
    return "ERROR: Cannot Divide by 0"
  return x % y

# Map operations to their functions using a dictionary
operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '**': exponent,
  '/': division,
  '%': modulus,
}

# Get user input
try:
  num1 = float(input("Enter: "))
  operation = input("Operation (+, -, *, **, /, %): ")
  num2 = float(input("Enter: "))
except ValueError:
  print("ERROR: Invalid Input: Enter Numerical Values")
else:
  # Validate if user input is valid
    if operation in operations:     # Retrieve function and print output
    result = operations[operation](num1, num2)
    print(f"Result: {result}")
  else:    # Print ERROR message
    print("ERROR: Invalid Input")
