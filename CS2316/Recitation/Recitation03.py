#Practice

phrase = "Sphinx of Black Quartz, Judge My Vo"

print({char:index for index,char in enumerate(phrase.split())})

class Animal :
	def __init__(self, species, weight, num_legs) :
		self.species = species	
		self.weight = weight
		self.num_legs = num_legs

	def __lt__ (self , other) :
		return self.weight < other.weight

	def __eq__ (self, other) :
		return self.species == other.species

animal1 = Animal("Dog" , 30, 4)

#Alias
original = [1,2,3,4,["a","b"]]
list1 = original #everything that happens to original, happens to list1 and vice versa

#Deep Copy
import copy as c
list2 = c.deepcopy(original)
print(list2) #looks the same as the original, and the original stays the same
original[4][0] = "ww" #changes original but not list2

#Shallow Copy
list3 = c.copy(original) #exact same as original
original[0] = 77 #changes original but not list3
original[4][0] = "zzzz" #changes the original and list3 because it only copies one level
print(original)
print(list3)
list4 = original[:] #another way of creating a shallow copy


