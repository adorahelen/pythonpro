class Card:
  """ A playing card. """
  RANKS = ["A", "2", "3", "4", "5", "6", "7",
           "8", "9", "10", "J", "Q", "K"]

  SUITS = ["c", "d", "h", "s"] # *클로버 스페이스 하트 다이아

  def __init__ (self, rank, suit):
      self.rank = rank
      self.suit = suit

 def __str__ (self):
     reply = self.rank + self.suit
     return reply


class Hand: 
   """ A hand of playing cards. """
   def __init__(self) :
      self.cards = []

   def __str__(self) :
     if self.cards:
        reply = ""
        for card in self.cards:
          reply += str(card) + " "
     else:
         reply = "<empty>"
     return reply 


   def clear(self):
     self.cards = []
   def add(self, card):
     self.cards.append(card)


   def give(self, card, other_hand):
     self.cards.remove(card)
     other_hand.add(card) 
   

   
