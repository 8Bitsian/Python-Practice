# Guess the Number: User provides a number and program outputs result (High or Low)
import random # Generate a random number
import sys # Used for clean exit

SECRET = random.randint(1, 100) # Generate a number between 1 and 100 (inclusive)
MAX_GUESSES = 10 # Cap the number of attempts

# Define main guessing number game function
def guess_num_game():
  print("------- Guess The Number Game -------")
  print("Generating Number Between 1 & 100...")
  print(f"You have {MAX_GUESSES} guesses.")
  print("-------------------------------------\n")

  attempts = 0
  while attempts < MAX_GUESSES:
    try: # Get user input
      guess_input = input("Enter ('X' to exit): ").strip()
      if guess_input.lower() == 'x': # User exits program
        print(f"\nExiting Game.\n")
        sys.exit() # Exit the program
      guess = int(guess_input)
      attempts += 1
    except ValueError:
      print("ERROR: Invalid Input. Enter a Numerical Value or 'X'.\n")
      
    # Check the guess
    if guess < SECRET:
      print(f"Too low! Attempts left: {MAX_GUESSES - attempts}")
    elif guess > SECRET:
      print(f"Too high! Attempts left: {MAX_GUESSES - attempts}")
    else:
      print(f"\n🎉 Correct!🎉  You guessed {SECRET} in {attempts} attempts.")
      return # Exit the function.game
      
  #If user loses the game
  print(f"\n👾 Game Over!👾  You ran out of guesses. The secret number was {SECRET}.")

# Start the game by calling the function
if __name__ == "__main__":
  guess_num_game()
