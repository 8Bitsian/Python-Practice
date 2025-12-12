# Guess the Number: User provides a number and program outputs result (High or Low)
import random # Generate a random number

# Generate a number between 1 and 100 (inclusive)
secret = random.randint(1, 100)

# Define guess_num function
def guess_num():
  # Get user input
  guess = int(input("Enter your guess: "))
  
  # Check if guess is less (or greater) than secret
  if guess < secret: # Check if guess is less than secret number
    print("Too low! Try again.")
    guess_num()
  elif guess > secret: # Check if guess is greater than secret number
    print("Too high! Try again.")
    guess_num()
  else: # If the guess is correct, congratulate the player
    print("Correct! You guessed the number.")

# Start the game by calling the function
guess_num()
