class Critter:
   def __init__(self, name, mood):
      self.name = name # public attribute 
      self.__mood = mood # private attribute


class Critter: 
... 
   def talk(self): 
      print(" \n I'm", self.name)
      print("Right now I feel", self.__mood, "\n")


class Critter:
... 
   def __private_method(self):
       print("This is a private method.") 


class Critter: 
...
   def public___method (self):
       print ("This is a public method.")
       self.__private__method()


crit = Critter(name = "poochie", mood = "happy")
crit.talk()
crit.public_method() 
 
