import random

def word_guessing_game():
    print("Welcome to Guess the Word Game!")
    print("Guess the three letter word at a time. You have 3 chances.\n")

    # List of words with hints
    words_with_hints = {
        "dog": "It's a common pet and very loyal.",
        "cat": "A pet that loves to purr.",
        "rat": "A small rodent.",
        "pig": "Lives on farms and loves mud.",
        "hen": "A bird that lays eggs."
    }

    # Shuffle and select a random word with its hint
    items = list(words_with_hints.items())
    random.shuffle(items)
    secret_word, hint = items[0]

    print(f"Hint: {hint}")  # Show the hint to the player
    attempts_left = 3

    while attempts_left > 0:
        print(f"\nAttempts left: {attempts_left}")
        guess = input("Guess a letter: ").lower()

        if guess in secret_word:
            print("Congratulations! You guessed it right!")
            print(f"The word was: {secret_word}")
            break
        else:
            print("Wrong guess!")
            attempts_left -= 1

    else:
        print(f"\nGame over! The word was: {secret_word}")

# Start the game
word_guessing_game()
