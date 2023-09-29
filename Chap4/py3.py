import random
target_number = random.randint(1, 100)

count = 0

print("                    " +"Welcome to 'Guess My Number'!")
print("")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
print("")

while True:
    try: 
      user_guess = int(input("Take a guess:"))
    except ValueError:
      print("RE:")
      continue

    count += 1

    if user_guess > target_number:
      print("Lower...")
    elif user_guess < target_number:
      print("Higer...")
    elif user_guess == target_number:
      print("You guessed it! The number was %d" %target_number)
      print("And it only took you %d tries!" %count)
      break

print("")
print("")
print("Press the enter key to quit.")      
