import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
display = ["_" for _ in range(word_length)]

guessed_letters = []
wrong_guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print(f"But you've already guessed {guess}")
        continue  # Skip the rest of the loop

    guessed_letters.append(guess)

    # Check guessed letter
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life...")
        wrong_guesses.append(guess)
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was '{chosen_word}'.")

    # Display current progress
    print(f"{' '.join(display)}")

    # Display wrong guesses
    if wrong_guesses:
        print(f"This word doesn't contain the letters: {', '.join(wrong_guesses)}")

    # Check if the player has won
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the current state of the hangman
    print(stages[lives])