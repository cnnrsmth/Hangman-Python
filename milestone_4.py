import random
from milestone_2 import get_favorite_fruits

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.
        """
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter.lower() == guess:
                    self.word_guessed[i] = letter
            self.num_letters = len(set(self.word) - set(self.word_guessed))
        else:
            # Step 1: Create an else statement
            # Step 2: Reduce num_lives by 1, print messages
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Ask the user to guess a letter.
        """
        while True:
            guess = input("Enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

# Test the Hangman class
if __name__ == "__main__":
    word_list = get_favorite_fruits()
    game = Hangman(word_list)
    
    while game.num_lives > 0 and '_' in game.word_guessed:
        print(f"Word to guess: {' '.join(game.word_guessed)}")
        game.ask_for_input()
        print("Updated list of guesses:", game.list_of_guesses)
        print("Updated word guessed so far:", game.word_guessed)
        print("Updated number of lives:", game.num_lives)

    if game.num_lives == 0:
        print(f"You lost! The word was: {game.word}")
    else:
        print(f"Congratulations! You guessed the word: {game.word}")
