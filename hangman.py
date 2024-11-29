import random

# List of words to choose from
word_list = ["python", "hangman", "challenge", "university", "programming"]

def choose_word(word_list):
    return random.choice(word_list)

def display_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + display_progress(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} tries left.")
        
        if set(word).issubset(guessed_letters):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nSorry, you've run out of guesses. The word was: {word}")

# Run the game
hangman()
