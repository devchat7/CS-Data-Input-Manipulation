#Object Oriented Programming
class Phone:
	# Defines characteristics / attributes
	def __init__(self, make, model, price):
		self.make = make
		self.model = model
		self.price = price

	# Defines behaviors / methods
	def drop_price(self) : 
		self.price -= 25
	def __eq__(self, other) : 
		return self.model == other.model
	def __repr__(self) : # a str representation of an object
		return f"{self.model} , {self.price}" #letter f allows us to put whatever we want in the curly brace
	def __str__(self) :
		return f"{self.model} worth ${self.price}" 
		

your_phone = Phone("Apple", "iPhone 11", 999)
bohong_phone = Phone("Google","X", 1211)
print(your_phone == bohong_phone) #calls the __eq__ method

# it calls __repr__ if no __str__ method is availbale or if
# the object is being printed from within a different data structure

phone = [bohong_phone, your_phone, your_phone]
print(phone)

print("cat {} hat".format("in the"))
print(f"cat {3} hat")

#Lecture 8
class Card:
	
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __repr__(self) : 
		return f"{self.rank} of {self.suit}"

	def __eq__(self, other) : 
		return self.suit == other.suit and self.rank == other.rank

	def __lt__(self,other) :
		return self.rank < other.rank

c1 = Card("spades" , 3)
c2 = Card("spades" , 3)
print(c1 == c2)
card_list = [Card("spades",7), Card("clubs",2), Card("clubs",6)]
card_list.sort()
print(card_list)

import random
a_card = Card(random.randrange(0,13),random.randrange(0,4))
print(a_card)

class Deck:
	def __init__(self):
		self.cards = [Card(rank,suit) for rank in range(13) \
		for suit in range(4)]


	def __repr__(self):
		return f"A deck of {len(self.cards)} cards."

	def print_all(self):
		print("Here is the deck of cards")
		for card in self.cards:
			print(card)

# create a Deck object and print it out
mydeck = Deck() 
print(mydeck)

#Print out the first three cards of the deck mydeck

print(mydeck.cards[0:3])


	def shuffle(self):
		num_cards = len(self.cards)
		for i in range(num_cards):
			j = random.randint(0, num_cards-1)
			(self.cards[i], self.cards[j]) = \
			(self.cards[j], self.cards[i])       #swap

	def deal_random(self):       # removes card after dealing
		random_place = random.randint(0, len(self.cards)-1)
		dealt_card = self.cards[random_place]
		del self.cards[random_place]
		return dealt_card
        



