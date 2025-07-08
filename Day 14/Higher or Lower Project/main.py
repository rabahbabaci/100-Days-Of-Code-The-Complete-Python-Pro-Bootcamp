from art import logo, vs
import random
from game_data import data

def display_option(option):
    """Formats a single option for display."""
    return f"{option['name']}, a {option['description']}, from {option['country']}"

def compare_options(option_a, option_b, user_choice):
    """Returns True if user's guess is correct."""
    if user_choice == 'A':
        return option_a["follower_count"] >= option_b["follower_count"]
    else:
        return option_b["follower_count"] > option_a["follower_count"]

def grab_two_options():
    """Returns two different random options."""
    option_a = random.choice(data)
    option_b = random.choice(data)
    while option_a == option_b:
        option_b = random.choice(data)
    return option_a, option_b

def play():
    print(logo)
    score = 0
    game_over = False

    # Start with two random options
    option_a, option_b = grab_two_options()

    while not game_over:
        print(f"\nCompare A: {display_option(option_a)}")
        print(vs)
        print(f"Against B: {display_option(option_b)}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        is_correct = compare_options(option_a, option_b, user_choice)

        if is_correct:
            score += 1
            print(f"\n✅ You're right! Current score: {score}")
            # B becomes next round's A; pick new B
            option_a = option_b
            option_b = random.choice(data)
            while option_b == option_a:
                option_b = random.choice(data)
        else:
            print(f"\n❌ Sorry, that's wrong. Final score: {score}")
            game_over = True

# Start the game
play()