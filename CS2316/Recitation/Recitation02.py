# General Notes
	# Mutable means changeable - review data types which are mutable and not
	# Boolean is always false if 0 because that represents empty set. True if not 0
	# Ordered means the order of it matters. "ab" != "ba"
	# When using a for loop for a dictionary, it iterates through the key and not the value
# Lambda
	# <function name> = lambda <parameters> : <expression>
	# ex. sq_area = lambda width, length: width * length
	# or create for single use
		# lambda <parameters> : <expression>
		# ex. sorted([2,"b"]), (1,"a"), key = lambda x: x[0]) <- sorts based on the 0 index
# Conditionals
	# val_if_true if condition else val_if_false
	# value_if_true if condition else val_if_elif if condition else val_if_false
# Operators
	# Multiplication
		# "hi" * 2 = "hihi"
	# Division (/)
		# always a float, includes repeating decimals
	# Integer Division (//)
		# how many times does a value go into another (the floor, no remainder)
	# Logical Operators
		# not, and, or
# list comprehension
	# item_expression for variable in iterable_object if condition
		# [num for in a if num % 2 == 0] <- a = range(10)
		# appends num to the num list pretty much
		# biggest advantage is that these comprehensions are way more efficient

		#Practice
			# Write a list comprehension that produces a list of words where each word is a word
			# from the list with its first and last letters swapped, list is word_list

word_list = ["how", "the", "turn", "tables"]
a = []
for word in word_list :
		a.append(word[-1] + word[1:-1] + word[0])
print(a)

# OR

'''
a2 = word[-1] + word[1:-1] + word[0]for word in word_list
print(a2)
'''
# Dictionary Comprehension
	# maps each of the characters in the phrase to the last position in the phrase if the character
	# is not a vowel
phrase = "supercalifragilisticexpialidocious"
my_dict = {}
for slider in range(len(phrase)) :
	if phrase[slider] not in "aeiou" :
		my_dict[phrase[slider]] = slider



