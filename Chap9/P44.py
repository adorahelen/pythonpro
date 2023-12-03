class Critter:
    # ... (Class implementation details not provided)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name == "":
            print("Critter's name can't be an empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

    name = property(get_name, set_name)


# Creating an instance of Critter
crit = Critter("Poochie")

# Accessing the name property using get_name
print(crit.get_name())  # Output: Poochie

# Changing the name property using set_name
crit.set_name("")  # Output: Critter's name can't be an empty string.
crit.set_name("Randolph")  # Output: Name change successful.

# Accessing the updated name property
print(crit.get_name())  # Output: Randolph



