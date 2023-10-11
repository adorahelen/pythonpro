import random

# Create a list of pre-defined words
words = ['difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university']

# Select a word at random
selected_word = random.choice(words)

# Inform the player about the length of the selected word
word_length = len(selected_word)

print(f"Welcome to the Word Guessing Game!")
print(f"The selected word has {word_length} letters.")

# Create a set to store the guessed letters
guessed_letters = set()

# Initialize the number of remaining attempts
remaining_attempts = word_length

while remaining_attempts > 0:
    # Display the current state of the word with underscores
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in selected_word])
    print(f"Current word: {display_word}")
    print(f"Remaining attempts: {remaining_attempts}")

    # Check if the player has guessed the word
    if display_word == selected_word:
        print(f"Congratulations! You've guessed the word: {selected_word}")
        break

    # Prompt the user to enter a guessed letter
    user_guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is valid
    if len(user_guess) == 1 and user_guess.isalpha():
        if user_guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif user_guess in selected_word:
            guessed_letters.add(user_guess)
            print("Correct guess!")
        else:
            print("Incorrect guess.")
            remaining_attempts -= 1
    else:
        print("Invalid input. Please enter a single letter.")

# If the loop ends and the player hasn't guessed the word, they've run out of attempts
if remaining_attempts == 0:
    print(f"You've used up all your attempts. The correct word was {selected_word}.")
