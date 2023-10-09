import random

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')

Select_words = random.choice(words)


Jumbled_word = ''.join(random.sample(Select_words, len(Select_words)))

print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")
print(f"Jumbled word: {Jumbled_word}")

Your_guess = input("Your guess: ")

if Your_guess.lower() == Select_words:
    print(f"Congraturation. That is correct: {Select_words}")
else:
    print(f"That is not correct. The word was: {Select_words}")
