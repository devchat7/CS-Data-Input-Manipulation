#lecture 5 notes
import sys
print(sys.argv) # prints out the arguments included when the code was run

"""
for num in range(int(sys.argv[1])) :
	print(num) # 0, 1, 2, 3, 4
"""

#list comprehension
# [expression for item in iterable if expression] <- don't always need if 
print([ i * 2 for i in range(10) if i % 2 == 0 ])
print([letter for letter in "jackets"])

oldlist = ([ i * 2 for i in range(10) if i % 2 == 0 ])
newlist = [i for i in oldlist if i%3 == 0]
print(newlist)

sentence = "the best day of the week is friday"
print([len(word) for word in sentence.split() if word != "the"])

#dictionary comprehension
import math
dict1 = {i:i**2 for i in range(10)}
dict2 = {key : val for key, val in [(1,"a"), (2,"b"), (3, "c")]}
print({math.sqrt(x):x for x in range(3,6)})

print({x : str(x) * x for x in range(1,6)})

#Practice
word_list = ["wow", "that", "is", "cool"]
print([word for word in word_list if word[0] == word[-1]])

print([word[-1] + word[1:-1] + word[0] for word in word_list])

word = "mcdaniel"
print({char : word.index(char) for char in word if not char in "aeiou"})

phrase = "cs2316 is my favorite class" 
print({word:pos for (pos,word) in enumerate(phase.split())})