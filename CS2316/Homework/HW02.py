import csv
from pprint import pprint
import requests
import json
from bs4 import BeautifulSoup
import re

### DO NOT MODIFY THE FOLLOWING METHOD ###
def date_cleaner(string):
	mapping = {"January":"01", "February":"02", "March":"03",
				   "April":"04",   "May":"05",      "June":"06",
				   "July":"07",    "August":"08",   "September":"09",
				   "October":"10", "November":"11", "December":"12"}
	MM = mapping[string.split()[0]]
	DD = string.split(",")[0].split()[1]
	DD = "0" + DD if len(DD) == 1 else DD
	YYYY = string.split(",")[1].strip()
	date_str = f"{MM}/{DD}/{YYYY}"
	return date_str
##########################################

def shrek_script(file_name, output_file):
	line_num = 0
	total_words = 0
	lister = []
	num_words = 0
	
	with open (file_name + ".txt", "r") as f:  #encoding = "utf8"
		script = f.readlines()
		
	for line in script:
		line_num += 1
		shrek_present = "Shrek" in line
		num_words = len(line.split())
		total_words += num_words
		line_text = line.strip()
		lister.append([line_num, num_words, total_words, shrek_present, line_text])
	
	with open (output_file + ".csv", "w") as fout:
		writer = csv.writer(fout)
		writer.writerows(lister)
	return lister
	
def csv_parser(filename):
	with open (filename, "r", encoding = "utf8") as f:
		reader = csv.reader(f)
		reader_list = list(reader)
		#print(reader_list)
	arr = []
	lister = []
	parser = []
	header = ["ID", "IsMovie", "IsShow", "Title", "Director/s", "CastList", "CastSize", "Rating", "DateAdded", "IsHorror", "Synopsis"]
	
	for line in reader_list[1:]:
		synopsis2 = ""
		iD = line[0]
		isMovie = line[1] == "Movie"
		isShow = line[1] == "TV Show"
		title = line[2]
		
		if len(line[3]) == 0:
			directors = "NIA"
		else:
			directors = line[3]

		rating = line[8]

		if (len(line[6].split()) == 0):
			dateAdded = "NIA"
		else:
			dateAdded = date_cleaner(line[6])

		if "Horror" in line[10]:
			isHorror = "Horror"
		else:
			isHorror = "Not Horror"
		
		castlist1 = line[4]
		castlist = list(castlist1.split(","))
		
		for i in range(len(castlist)):
			name = castlist[i].lstrip()
			if ' ' in name:
				name = name[0] + ". " + name.split()[-1]
				castlist[i] = name
			else:
				castlist[i] = name

		if line[4] == "":
			castlist = []
		
		castSize = len(castlist)

		if castlist == "":
			castSize = 0
		
		synopsis1 = line[-1].split()[:10]
		for each in synopsis1:
			synopsis2 += each + " "
			synopsis = synopsis2[:-1] + "..."
		parser.append([iD,isMovie,isShow,title,directors,castlist,castSize,rating,dateAdded,isHorror,synopsis])
	parser.insert(0,header)
	return parser[:3]

def json_parser(filename):
	with open (filename) as fish:
		data = json.load(fish)
	
	#for line in data:
	#	iD = 

def horror(csv_data, json_data, filename):
	pass

def character_info(page):
	r = requests.get(f"https://api.disneyapi.dev/characters?page={page}")
	data = r.json()["data"]
	characters = []
	for var in range(0 , len(data)):
		tv = "None"
		if (len(data[var]["tvShows"])) != 0:
			tv = data[var]["tvShows"]
		if (len(data[var]["films"])) > 0:
			characters.append((data[var]["name"], data[var]["_id"],data[var]["films"],tv))
	characters.sort()
	return sorted(characters, key = lambda characters:len(characters[2]),reverse = True)

def glee_dict(filename):
	with open(filename, encoding = "utf8") as f:
		data = f.read()
	soup = BeautifulSoup(data, "html.parser")
	tags = soup.find_all("td")
	parser = []
	for each in tags:
		arr = []
		season = each.find("td",{"class":"column-1"})
	
def colorful_film():
	pass

if __name__ == "__main__":
	#pprint(shrek_script('shrek', 'shrek_clean'))

	pprint(csv_parser('netflix.csv'))

	#pprint(json_parser('netflix.json'))

	# clean_csv = csv_parser('netflix.csv')
	#clean_json = json_parser('netflix.json')
	# pprint(horror(clean_csv, clean_json, 'double_analysis.json'))

	#print(character_info(49))
	#print(character_info(72))

	#print(glee_dict('glee.html'))

	# print(colorful_film())

	



