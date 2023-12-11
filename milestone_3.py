from milestone_2 import generate_word

while True:
    guess = input("Please input a letter:")

    if guess.isalpha() and len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in generate_word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")