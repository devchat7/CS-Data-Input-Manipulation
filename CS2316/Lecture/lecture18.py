import re

pattern = "nn"
text = "Does the beginning of the text match?"
match = re.search(pattern, text)
print(match)  # a Match object or None
if match:
	s = match.start()
	e = match.end()
	print(match.group())


'''
pattern = "[a-c][a-c][a-c]" #only 2 matches because there cannot be overlaps
text = "cabcab"
substring_list = re.findall(pattern, text)
print(substring_list)
for match in substring_list:
    print(f'Found {match}')
'''

#Practice
pattern = "3"
sentence = "Move the desks in rooms 123, 437, 329, 101, and 83."
substring_list = re.findall(pattern,sentence)
print(len(substring_list))

pattern = "[aeiou]"
sentence = "Move the desks in rooms 123, 437, 329, 101, and 83."
substring_list = re.findall(pattern,sentence)
print(len(substring_list))

pattern = "\d\d\d"
sentence = "Move the desks in rooms 123, 437, 329, 101, and 183."
substring_list = re.findall(pattern,sentence)
print(len(substring_list))

pattern = ""
sentence = "Move the desks in rooms 123, 437, 329, 101, and 83."
substring_list = re.findall(pattern,sentence)
print(len(substring_list))

print(re.findall("^[A-Za-z]+","A big rabbit")) #first letter
print(re.findall("[A-Za-z]+$","A big rabbit")) #last letter
print(re.findall("[A-Za-z]{3}\s","A big rabbit")) #words with 3 letters and then a whitespace

text = "I love CS2316."
pattern = r"[A-Z]"
replacement = "$"
newstring = re.sub(pattern, replacement, text)
print(newstring)

text = """My phone number is 770-333-5678 and Erin's phone
number is 404-404-1111 and Josh's phone number is 678-422-5678"""
pattern = " (\d{3})-"
matches = re.findall(pattern, text)
print(matches)

print(re.findall("[A-Z]*[a-z]+","The big dog"))


# Lecture 20
text = "12x34xx56xxx78xxxx910xx"
pattern = "[^x]x{2,3}[^x]"
matches = re.findall(pattern,text)
print(matches)

text1 = "My cat’s favorite toy is a mouse with a 9 volt battery."
print(re.findall(r"(.)[a9]",text1))