from milestone_2 import generate_word  # generate_word is defined in the milestone_2 module

def check_guess(guess):
    """
    Check if the guessed letter is in the word.
    """
    guess = guess.lower()  # Step 2: Convert the guess to lowercase

    if guess in generate_word:  # Step 3: Check if the guess is in the word
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    """
    Ask the user for a valid input.
    """
    while True:
        guess = input("Please input a letter:")

        if guess.isalpha() and len(guess) == 1:  # Step 2: Check if the input is a valid letter
            return
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

        check_guess(guess)  # Step 3: Call the check_guess function to check if the guess is in the word

# Step 4: Call the ask_for_input function to test the code
ask_for_input()

