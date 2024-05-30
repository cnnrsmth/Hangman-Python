import random
from milestone_2 import get_favorite_fruits, choose_random_word, get_user_guess, validate_guess

def check_guess(guess, word):
    """
    Check if the guessed letter is in the word.
    """
    # Step 2: Convert the guess into lower case
    guess = guess.lower()
    
    # Step 3: Check if the guess is in the word
    if guess in word.lower():
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(word):
    """
    Iteratively prompt the user to enter a valid guess.
    """
    while True:
        # Step 2: Get the user's guess
        guess = get_user_guess()

        # Step 3: Validate the guess
        if validate_guess(guess):
            # Call the check_guess function to check if the guess is in the word
            check_guess(guess, word)
            break
        else:
            # Print an error message if the input is not valid
            print("Invalid letter. Please, enter a single alphabetical character.")

def main():
    # Step 1: Create a list of favorite fruits
    word_list = get_favorite_fruits()

    # Step 2: Print the word list
    print(word_list)

    # Step 3: Choose a random word from the list and print it
    word = choose_random_word(word_list)
    print(f"Randomly chosen word: {word}")

    # Step 4: Call the ask_for_input function
    ask_for_input(word)

if __name__ == "__main__":
    main()
