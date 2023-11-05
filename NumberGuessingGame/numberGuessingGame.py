import random

EASY_MODE = 10
HARD_MODE = 5

def check_answer(guess,computer_guess,attempts):
    if guess == computer_guess:
        print(f"You got it! The answer was {computer_guess}")
    elif guess < computer_guess:
        print("Too low.")
        return attempts - 1
    elif guess > computer_guess:
        print("Too high.")
        return attempts - 1

def set_difficulty():
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if mode == "hard":
        return HARD_MODE
    elif mode == "easy":
        return EASY_MODE

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    computer_guess = random.randint(1, 100)

    attempts = set_difficulty()

    guess = 0
    while guess != computer_guess:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess,computer_guess,attempts)

        if attempts == 0:
            print("You've ran out of guesses. You lose.")
            return
        elif guess != computer_guess:
            print("Guess again.")

game()