# Basic Calculator: User provides two numbers and selects an operation (+, -, *, **, /, %)
import operator # Used for function-based versions of operators
import sys # Used for clean exit

# Map operations to functions from the operator module
OPERATIONS = {
  '+': operator.add,
  '-': operator.sub,
  '*': operator.mul,
  '**': operator.pow,
  '/': operator.truediv,
  '%': operator.mod,
}

# Define user input function
def get_input(message):
  while True:
    try:
      user_input = input(message).strip()
    except EOFError:
      print("\nInput stream ended unexpectedly. Exiting Calculator.\n")
      sys.exit()

    if user_input.lower() == 'x': # User exits program
      print("\nExiting Calculator.\n")
      sys.exit()
    try:
      return float(user_input)
    except ValueError:
      print("\nERROR: Invalid Input: Enter a Numerical Value or 'X'.\n")

# Define main calculator function
def calculator():
  print("----- Simple Calculator -----")
  print("Operations: +, -, *, **, /, %")
  print("Type 'X' at anytime to quit.")
  print("Type 'C' at anytime to clear.")
  print("-----------------------------\n")

  total = None # Initialize variable to hold running total

  while True:
    try:
      # Get initial input (Check if there's a running total)
      if total is None:
        # Initial run or after 'C' command: Prompt for initial number
        num1 = get_input("Enter ('X' to exit): ")
      else:
        print(f"Total: {total}")
        num1 = total
      
      # Get operation
      operation = input("Operation (+, -, *, **, /, %) ('C' to clear): ").strip()

      if operation.lower() == 'x':
        print("\nExiting Calculator.\n")
        break
      elif operation.lower() == 'c':
        total = None
        print("\nCalculator Cleared.\n")
        continue

      if operation not in OPERATIONS:
        print("\nERROR: Invalid Input: Enter an Operation.\n")
        continue
      
      # Get second input
      num2 = get_input("Enter ('X' to exit): ")
      
      # Calculate
      calculation = OPERATIONS[operation]

      # Check for Zero Division for division and modulus
      if (operation in ('/', '%')) and num2 == 0:
        print("\nERROR: Zero Division: Cannot Divide by 0.\n")
        continue

      result = calculation(num1, num2)
      total = result # Update running total
      
      # Print Result
      print(f"\n--- Calculation: {num1} {operation} {num2} = {result}\n")
    
    # Catch all unhandled exceptions and reset the total
    except Exception as e:
      print(f"\nERROR: Unexpected Error Occured: {e}...")
      print("Resetting Calculator...\n")
      total = None # Resets total after Error
      continue

# Run the calculator
if __name__ == "__main__":
  try:
    calculator()
  except SystemExit:
    pass # Catch sys.exit() from get_numeric_input
