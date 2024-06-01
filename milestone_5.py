import random
from milestone_2 import get_favorite_fruits

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game with a list of words and number of lives.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._select_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _select_random_word(self):
        """
        Select a random word from the word list.
        """
        return random.choice(self.word_list)

    def _update_word_guessed(self, guess):
        """
        Update the word guessed list with the correct guess.
        """
        for i, letter in enumerate(self.word):
            if letter.lower() == guess:
                self.word_guessed[i] = letter
        self.num_letters = len(set(self.word) - set(self.word_guessed))

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.
        """
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Ask the user to guess a letter.
        """
        while True:
            guess = input("Enter a single letter: ").lower()
            if not self._is_valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

    def _is_valid_guess(self, guess):
        """
        Check if the guess is a single alphabetical character.
        """
        return len(guess) == 1 and guess.isalpha()

def play_game(word_list):
    """
    Play the Hangman game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            print(f"Word to guess: {' '.join(game.word_guessed)}")
            game.ask_for_input()
            print("Updated list of guesses:", game.list_of_guesses)
            print("Updated word guessed so far:", game.word_guessed)
            print("Updated number of lives:", game.num_lives)
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    word_list = get_favorite_fruits()
    play_game(word_list)
