import random

# ASCII art dictionary
ascii_art = {
    "rock": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    "paper": '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    "scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

# Game rules dictionary
win_map = {
    "rock":     {"rock": "It's a tie!", "paper": "You lose!", "scissors": "You win!"},
    "paper":    {"rock": "You win!", "paper": "It's a tie!", "scissors": "You lose!"},
    "scissors": {"rock": "You lose!", "paper": "You win!", "scissors": "It's a tie!"}
}

choices = list(ascii_art.keys())

def get_user_choice():
    print("\nChoose:")
    for i, choice in enumerate(choices):
        print(f"{i}: {choice.title()}")
    try:
        index = int(input("===>: "))
        if index not in range(len(choices)):
            raise ValueError
        return choices[index]
    except ValueError:
        print("❌ Invalid input. Try again.")
        return None

def play_round():
    user_choice = None
    while user_choice is None:
        user_choice = get_user_choice()

    computer_choice = random.choice(choices)

    print(f"\nYou chose:\n{ascii_art[user_choice]}")
    print(f"Computer chose:\n{ascii_art[computer_choice]}")
    print(f"Result: {win_map[user_choice][computer_choice]}")

# Main game loop
while True:
    play_round()
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing! 👋")
        break