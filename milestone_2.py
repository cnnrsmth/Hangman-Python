import random

def get_favorite_fruits():
    """
    Create and return a list of favorite fruits.
    """
    return ["Apple", "Banana", "Durian", "Dragonfruit", "Elderberry"]

def choose_random_word(word_list):
    """
    Select and return a random word from a list.
    """
    return random.choice(word_list)

def get_user_guess():
    """
    Prompt the user to enter a single letter and return the input.
    """
    return input("Enter a single letter: ")

def validate_guess(guess):
    """
    Check if the guess is a single alphabetical character.
    """
    return len(guess) == 1 and guess.isalpha()

def main():
    # Step 1: Create a list of favorite fruits
    word_list = get_favorite_fruits()

    # Step 2: Print the word list
    print(word_list)

    # Step 3: Choose a random word from the list and print it
    word = choose_random_word(word_list)
    print(f"Randomly chosen word: {word}")

    # Step 4: Get the user's guess
    guess = get_user_guess()

    # Step 5: Validate the guess and print appropriate message
    if validate_guess(guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

#When the script is imported into another script, the condition if __name__ == "__main__": 
# evaluates to False, and the main() function is not called. This prevents the main execution 
# code from running and allows the script's functions, classes, and variables to be used without 
# side effects.
if __name__ == "__main__":
    main()
