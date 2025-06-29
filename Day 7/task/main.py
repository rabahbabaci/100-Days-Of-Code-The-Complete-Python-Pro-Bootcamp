import random
from hangman_words import word_list
from hangman_art import logo

print(logo)

chosen_word = random.choice(word_list)
word_to_guess = ['_' for _ in chosen_word]
guessed_letters = []
correct_letters = []
lives = 6
game_over = False

while not game_over:
    print(f"Word to guess: {''.join(word_to_guess)}")
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in guessed_letters:
        if guessed_letter in correct_letters:
            print(f"🔁 You've already guessed '{guessed_letter}' and it was correct.")
        else:
            print(f"🔁 You've already guessed '{guessed_letter}' and it was wrong. You lose a life again.")
            lives -= 1
    else:
        guessed_letters.append(guessed_letter)
        if guessed_letter in chosen_word:
            correct_letters.append(guessed_letter)
            for i, letter in enumerate(chosen_word):
                if letter == guessed_letter:
                    word_to_guess[i] = guessed_letter
            print("✅ Good guess!")
        else:
            print(f"❌ '{guessed_letter}' is not in the word. You lose a life.")
            lives -= 1

    print(f"\n💡 Guessed so far: {', '.join(sorted(guessed_letters))}")
    print(f"❤️ Lives left: {lives}/6")

    if '_' not in word_to_guess:
        game_over = True
        print(f"\n🎉 YOU WON! The word was '{chosen_word}'.")
    elif lives == 0:
        game_over = True
        print(f"\n💀 GAME OVER! The word was '{chosen_word}'.")