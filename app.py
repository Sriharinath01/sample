# Import the random module to generate random numbers
import random

# Generate a random integer between 1 and 100 (inclusive)
secret_number = random.randint(1, 100)
attempts = 0

print("--- Welcome to the Number Guessing Game! ---")
print("I'm thinking of a number between 1 and 100.")

# Start an infinite loop that will run until the user guesses correctly
while True:
    try:
        # Ask the user for their guess and convert it to an integer
        guess = int(input("Enter your guess: "))
        attempts += 1  # Increment the attempt counter

        # Compare the guess to the secret number
        if guess < secret_number:
            print("Too low! Try again. 🤔")
        elif guess > secret_number:
            print("Too high! Try again. 😲")
        else:
            # If the guess is correct, congratulate the user and exit the loop
            print(f"🎉 Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break  # Exit the loop

    except ValueError:
        # Handle cases where the user enters something that is not a number
        print("Invalid input. Please enter a number.")