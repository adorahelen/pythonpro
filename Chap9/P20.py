print ("A new critter has been born!")
print ("HI. I'm Pochie")


class Critter:
    def __init__(self, name): 
        self.name = name

...
crit1 = Critter("Poochie")



class Critter:
... 
   def talk(self):
       print("Hi. I'm", self.name, "\n")
...
crit1.talk()


class Critter: 
     def __init__(self, name):
         self.name = name
...
crit1 = Critter("Poochie")
print (crit1.name)


class Critter:

...
  def __str__ (self):
      rep = "Critter object\n"
      rep += "name: " + self.name + "\n"
      return rep
...
   print(crit1)



