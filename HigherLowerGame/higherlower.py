from art import logo, vs
from game_data import data
import random, os


def compare(A, B):
    """Compares two dictionaries by the value of the key 'follower_count' and returns the one with bigger value in a form of str."""

    num_followers_A = A.get('follower_count')
    num_followers_B = B.get('follower_count')

    if num_followers_A > num_followers_B:
        return "A"
    else:
        return "B"


def format_data(account):
    """Takes a dictionary and returns it formatted"""
    return f"{account.get('name')}, a {account.get('description')}, from {account.get('country')}."


def game(A, B):
    total_score = 0

    while True:
        print(f"Compare A: {format_data(A)}")

        print(vs)

        print(f"Against B: {format_data(B)}")

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        bigger = compare(A, B)
        if choice == bigger:
            total_score += 1
            os.system('cls')
            print(logo)
            print(f"You're right! Current score: {total_score}")
            A = B
            B = random.choice([e for e in data if e != A])
        else:
            print(f"Sorry, that's wrong. Final score: {total_score}")
            return


account = random.choice(data)
B = random.choice([e for e in data if e != account])  # choosing random element that is different than A.

print(logo)

game(account, B)
