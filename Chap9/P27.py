class Critter:
   total = 0

 def __init__(self, name):
    Critter.total += 1

  @staticmethod 
   def status ():
     print("Total critters", Critter.total)


   Print(Critter.total)
   ...
   Print(crit1.total)

   class Critter:
   ...
      @staticmethod
      def status ():
          print("Total critters", Critter.total)

...
crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")

Critter.status() 
