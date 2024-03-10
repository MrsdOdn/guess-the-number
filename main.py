from art import logo
import random

answer = random.randint(1, 100)

print(logo)

print("Welcome to the Number Guessing Game!")
print("T'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {answer}.")
game_level_choice = input("Chose a difficulty.Type 'easy' or 'hard': ").lower()


def game_choice(game_level):
    if game_level == 'easy':
        attemps = 10
        return attemps
    else:
        attemps = 5
        return attemps


def guess_check(number):
    if number > answer:
        return "Too high."
    elif number < answer:
        return "Too low."
    else:
        return f"You got it! The answer was {answer}."


def play_game():
    your_attemps = game_choice(game_level_choice)
    while 0 < your_attemps:
        print(f"You have {your_attemps} attemps remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        print(guess_check(user_guess))
        if f"You got it! The answer was {answer}." == guess_check(user_guess):
            your_attemps = 0
        else:
            your_attemps -= 1
            if your_attemps == 0:
                print("You've run out of the guesses, you lose.")


play_game()