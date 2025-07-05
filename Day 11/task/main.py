import random
from art import logo

def clear():
    """Clears the terminal."""
    print("\033c", end="")

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the total score and handles aces + blackjack check."""
    score = sum(cards)
    # Check for Blackjack (21 with 2 cards)
    if score == 21 and len(cards) == 2:
        return 0
    # Convert 11 to 1 if score is over 21
    if score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score

def compare(user_score, comp_score):
    """Compares the user and computer scores and returns the result string."""
    if user_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 0:
        return "You lose 😱! Opponent has Blackjack."
    elif user_score == 0:
        return "You win 😎 with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 🙂"
    else:
        return "You lose 😤"

def play_game():
    clear()
    print(logo)

    user_cards = [deal_card(), deal_card()]
    comp_cards = [deal_card(), deal_card()]

    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)

    game_over = False

    while not game_over:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]} -- {comp_cards}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            draw = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if draw == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

# Game loop
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()