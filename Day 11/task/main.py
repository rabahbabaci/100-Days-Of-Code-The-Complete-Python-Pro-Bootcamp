from art import logo
import random

def clear():
    print("\033c", end="")

def deal_card():
    """Returns a random card from the deck."""
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def calculate_score(cards):
    score = sum(cards)
    # Handle ace (11 -> 1) if score > 21
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score

def evaluate_game(comp_cards, comp_score, player_cards, player_score):
    print(f"   Your final hand: {player_cards}, final score: {player_score}")
    print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")

    if player_score > 21:
        return "You lost 😭! Busted!"
    elif comp_score > 21:
        return "You won! 🎉 Computer busted."
    elif comp_score == player_score:
        return "It's a Draw ::::|"
    elif player_score > comp_score:
        return "You won!!! 🎉"
    else:
        return "You lost!"

# ─────────────────────────────
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while input("Wanna play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    print(logo)

    # Deal initial cards
    computer_cards = [deal_card()]
    player_cards = [deal_card(), deal_card()]
    computer_score = calculate_score(computer_cards)
    player_score = calculate_score(player_cards)

    game_over = False

    while not game_over:
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if player_score == 21 or player_score > 21:
            game_over = True
        else:
            another = input("Type 'y' to get another card, type 'n' to pass: ")
            if another == 'y':
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
            else:
                game_over = True

    # Computer plays if player hasn't busted
    while computer_score < 17 and player_score <= 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final result
    print(evaluate_game(computer_cards, computer_score, player_cards, player_score))
