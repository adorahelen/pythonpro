name = str(input("Hi. What's your name?"))
age = int(input("And how old are you?"))
weigh = int(input("Okay, last question. How many pounds do you weigh?"))

#DogAge = age/7
pound = weigh*2.20462

print("")

print("Did you know that you're just", age/7, " in dog years?")

print("")

print("But you're also over", age*365*24*60*60, "seconds old.")

print("")

print("If a small child were trying to get your attention, your name would become:")
print(name*5)
print("")

print("Did you know that on the moon you would weigh only", pound/6, "pounds?")
print("But on the sun, you'd weigh", pound*27.1, "<but, ah... not for long>.")

print("")
print("Press the enter key to exit.")
