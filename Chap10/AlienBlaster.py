Class player:
 def blast (self, enemy): #에너미라는 인자를 받아온다.
  print ("The player blasts an enemy.")
  enemy.die()

Class Alien:
 def die (self):
  print ("Good-bye, cruel universe.")

Hero = Player() #인스턴스 생성
invader = Alien() 
hero.blast(invader) # 


Class Player:
 def blast(self, enemy):
  print ("The Player blasts an enemy.")
  enemy.die()

...
hero.blast(invader)

