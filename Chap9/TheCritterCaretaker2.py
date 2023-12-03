import random


class Critter(object):
    """A Virtual Pet"""
    def __init__(self, name, hunger=random.randrange(0, 16), boredom=random.randint(0, 15)):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        print(hunger)
        print(boredom)

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "PISSED OFF!"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def play(self, fun=4):
        print("How many hours would you like to play with", self.name, "?(0-8)")
        fun = int(input("-----\t"))
        print("Wheeee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def eat(self, eat=4):
        print("How many meals would you like to feed", self.name, "?(0-8)")
        eat = int(input("------\t"))
        print("Brruppp. Thank youuuu hehe.")
        self.hunger -= eat
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def display(self):
        print("Hunger:\t", self.hunger)
        print("Boredom:\t", self.boredom)
        self.__pass_time()


class Food:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_level(self):
        return self.level

    def set_critter_level(self, critter):
        critter.hunger -= self.level
        if critter.hunger < 0:
            critter.hunger = 0
        critter.__pass_time()


def main():
    crit_name = input("What do you want to name your critter?:\t")
    crit = Critter(crit_name)

    food1 = Food("Dry Food", 3)
    food2 = Food("Meat", 5)
    food3 = Food("Vegetables", 2)

    choice = None
    while choice != "0":
        print("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter's feelings
        2 - Feed your critter
        3 - Play with your critter
        4 - See hunger and boredom
        5 - Feed your critter with a snack
        """)

        choice = input("Choice:\t")
        print()

        if choice == "0":
            print("Good-bye")

        elif choice == "1":
            crit.talk()

        elif choice == "2":
            crit.eat()

        elif choice == "3":
            crit.play()

        elif choice == "4":
            crit.display()

        elif choice == "5":
            print("Select a snack:")
            print("1 -", food1.name)
            print("2 -", food2.name)
            print("3 -", food3.name)
            snack_choice = input("Choice (1-3):\t")
            if snack_choice == "1":
                food1.set_critter_level(crit)
            elif snack_choice == "2":
                food2.set_critter_level(crit)
            elif snack_choice == "3":
                food3.set_critter_level(crit)
            else:
                print("Invalid snack choice.")

        else:
            print("Your choice is invalid")


main()

input("Press Enter key to exit")

