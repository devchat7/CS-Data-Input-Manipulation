#Lecture 13
'''
with open("pride_prejudice.txt","r", encoding="utf8") as f:
		#text1 = f.read() # reads the entire text into a str (read)
		#text2 = f.readline() #advances the curser down and reads each line (readline)
		#text3 = f.readline() 
	lines = f.readlines() #uses /n to signify the next line into a list
print(lines[:10])
with open("text_file.txt","w") as outfile:
    outfile.write("one\ntwo\nthree")  #type "type text_file.txt" in command prompt to see it

print("\n\t\\\"")
print(len("\n\t\\\"")) # prints 4 

def num_passengers():
	a = []
	with open("airtravel.csv" , "r") as infile: 
		lines = infile.readlines()
	datalines = lines[1:] #removes the header line
	print(datalines)
	for line in datalines:
		line = line.strip()
		pieces = line.split(",")
		if len(pieces) < 4 :
			continue
		value = int(pieces[3])
		a.append(value)
		print(line)
	print(a)	

num_passengers()

'''

'''
with open("pride_prejudice.txt","r") as f:
        # text1 = f.readline() 
        # text2 = f.readline()
        # text3 = f.readline()  # advances the curser
    lines = f.readlines() # a list of lines
print(lines[:10])
with open("text_file.txt","w") as outfile:
    outfile.write("one\ntwo\nthree") 
print("\n\t\\\"")
print(len("\n\t\\\""))
def num_passengers():
    with open("airtravel.csv","r") as infile:
        lines = infile.readlines()
    datalines = lines[1:]  # remove the header line
    #print(datalines)
    for line in datalines:
        line = line.strip()
        pieces = line.split(",") 
        if len(pieces) < 4:
            continue
        value = int(pieces[3])
        print(value) 
num_passengers()
'''

#lecture 14


# answer to text example from lecture 13
import string
def remove_punctuation(file1,file2):
	with open(file1,"r") as infile:
		text = infile.read()
	out_text = ""
	for ch in text:
		if ch not in string.punctuation:
			out_text += ch
	with open(file2,"w") as outfile:
		outfile.write(out_text)
	
remove_punctuation("course_schedule.txt", "course_schedule_new.txt")
# CSV reader example

import csv
with open("countries.csv") as fin:  
    reader = csv.reader(fin)
    data_list = list(reader) # this gives us a list of countries
    #print(data_list)
count = 0
for country in data_list[1:]:
    if "africa" in country[1].lower():
        count += 1
print(count)
