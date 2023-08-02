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

