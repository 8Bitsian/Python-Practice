# Basic Calculator: User provides two numbers and selects an operation (+, -, *, **, /, %)

# Define functions for each arithmetic operation
def add(x, y):
  """Function to perform addition"""
  return x + y
def subtract(x, y):
  """Function to perform subtraction"""
  return x - y
def multiply(x, y):
  """Function to perform multiplication"""
  return x * y
def exponent(x, y):
  """Function to perform exponenation"""
  return x ** y
def division(x, y):
  """Function to perform division"""
  return x / y
def modulus(x, y):
  """Function to perform division"""
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
num1 = float(input("Enter: "))
operation = input("Operation (+, -, *, **, /, %): ")
num2 = float(input("Enter: "))

# Validate if user input is valid
if operation in operations:
  # Retrieve function and print output
  result = operations[operation](num1, num2)
  print(f"Result: [result]")
else
  # Error message
  print("ERROR: Invalid Input")
