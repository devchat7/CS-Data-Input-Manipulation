# Card class changes made during the end of lecture7
import random
class Card:
	ranks = ["Ace","2","3","4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
	suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

	def __init__(self, rank, suit):  # rank and suit are ints
		self.rank = rank
		self.suit = suit

	def __repr__(self):      # returns a string version of the object
		return self.ranks[self.rank] + " of " + self.suits[self.suit]

	def __eq__(self,other):
		return self.rank == other.rank and self.suit == other.suit

	def __lt__(self,other):
		selfrank = 13 if self.rank == 0 else self.rank
		otherrank = 13 if other.rank == 0 else other.rank
		return selfrank < otherrank	

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

		

mydeck = Deck() 
yourdeck = mydeck

print(mydeck)
print(mydeck.cards[0:3])

# shuffle the deck called mydeck
#mydeck.shuffle()

# deal two random cards from the deck
card1 = mydeck.deal_random()
card2 = mydeck.deal_random()

# print out which card was higher calling the Card class’s __gt__ method
print(card1 if card1>card2 else card2)

#print(mydeck > yourdeck)
print(mydeck == yourdeck)



# import random
# a_card = Card(random.randrange(0,13),random.randrange(0,4))
# print(a_card)

# card_list = [Card(0,1),Card(1,1),Card(2,1)]
# print(card_list[0])
# print(card_list)

# mycard = Card(0,0)
# yourcard = Card(1,0)
# print(mycard == yourcard)
# print(mycard > Card(12,0))

# alist = [Card(rank,suit) for rank in range(13) \
# for suit in range(4)]
# print(alist)








