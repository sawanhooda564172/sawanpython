import random

# 1. Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Random Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# 2. Keep asking until the user guesses correctly
while True:
    # Ask the user to enter a guess
    guess = int(input("Enter your guess: "))
    attempts += 1

    # 3. Compare the guess with the random number
    if guess < secret_number:
        # 4. If the guess is too low
        print("Too Low! Try Again.")
    elif guess > secret_number:
        # 5. If the guess is too high
        print("Too High! Try Again.")
    else:
        # 6. Correct guess
        print(f"Congratulations! You guessed the number {secret_number} correctly.")
        print(f"Total number of attempts: {attempts}")
        break