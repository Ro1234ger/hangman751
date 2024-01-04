import random

create_fruit_name_list = {"apple","peach","melon","lemon","grape"}
word_list = list(create_fruit_name_list)
generate_word = random.choice(word_list)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game with the given parameters.

        Parameters:
        - word_list (list): A list of words for the game.
        - num_lives (int): Number of lives the player starts with (default is 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._choose_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _choose_word(self):
        """
        Choose a random word from the word_list.
        """
        generate_word = random.choice(self.word_list)
        return generate_word

    def check_guess(self,guess):
        """
        Check if the guessed letter is in the word.
        """
        guess = guess.lower()  
        # Convert the guess to lowercase

        if guess in self.word:  
            # Check if the guess is in the word
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        """
        Ask the user for a valid input.
        """
        print(self.list_of_guesses)
        print(f"There are {self.num_letters} letters in the word.")
        num_of_guesses = 0

        while True:
            guess = input("Please input a letter:")

            if not guess.isalpha() or len(guess) != 1:  
                # Check if the input is a valid letter
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:  
                # Check if the guess is already in list_of_guesses
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  
                # Call the check_guess method to check if the guess is in the word
                self.list_of_guesses.append(guess)  
                # Append the guess to list_of_guesses

                if '_' not in self.word_guessed:
                    print("Congratulations! You guessed the word.", self.word)
                    # Exit the loop if the word is completely guessed
                    break
                elif guess not in self.word:
                    incorrect_guesses += 1

            if incorrect_guesses == self.num_lives:
                print("Game over. You ran out of lives. The word was:", self.word)
                # Exit the loop if the player runs out of lives
                break
            
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()