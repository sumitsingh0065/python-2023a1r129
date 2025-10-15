import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (or type 'quit' to exit): ")

        if guess.lower() == 'quit':
            print(f"The secret number was {secret_number}. Better luck next time!")
            break

        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f" Congratulations! You guessed it in {attempts} tries!")
            break

number_guessing_game()
