from art import logo
import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def guess_check(user_guess, chosen_num):
    if user_guess == chosen_num:
        return 0
    elif user_guess < chosen_num:
        return "Too low."
    else:
        return "Too high."

def play():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    chosen_num = random.randint(1, 100)
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()
    attempts = EASY_ATTEMPTS if difficulty == "easy" else HARD_ATTEMPTS
    game_over = False

    while not game_over:
        print(f"\nYou have {attempts} attempts remaining.")

        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        result = guess_check(guess, chosen_num)
        if result == 0:
            print(f"🎉 You got it! The answer was {chosen_num}.")
            break

        print(result)
        attempts -= 1
        game_over = attempts == 0

        if not game_over:
            print("Guess again.")

    if game_over:
        print(f"😢 You've run out of guesses. The number was: {chosen_num}.")

    return input("Play again? Type 'yes' or 'no': ").lower() == 'yes'

# Game loop
while play():
    pass

print("\n👋 Have a good day!")
