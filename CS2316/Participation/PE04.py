import json, csv
from pprint import pprint


def read_csv(input_file):
	'''
	1.  Read the HighestGrossers.csv using CSV. Include the parameter encoding = "utf8"
			as a parameter in the open() function. Follow 1,3,4,5 for all row EXCEPT the first row,
			(the first row should be unchanged):

			1. If the 'GENRE' is not specified, insert "N/A" into the empty slot
			2. Change index 0 of first row '\ufeffYEAR' to 'YEAR'
			3. Exclude the 'MPAA RATING' column.
			4. Make the column 'TOTAL FOR YEAR' and 'TOTAL IN 2019 DOLLARS' into an int type (i.e. '$204,887,848 ' to 204887848)
			5. Make the column 'TICKETS SOLD' and 'YEAR' into an int type (i.e. '2,22,96,379' to 22296379 and '1996' to 1996)

			Output:
			[
				...
				etc.
				...]

	'''
	with open("HighestGrossers.csv","r", encoding="utf8") as foud:
		lines = foud.readlines()
		print(lines) 

def export_json(cleaned_list, output_file):
	"""
  2.  Using the extracted list from `read_csv()`, create a dictionary that maps each movie name to an
	  inner dictionary, where the inner dictionary's keys are
		1. "Year" (year the movie was released in)
		2. "Genre" (genre of the movie)
		3. "Average Ticket Price" (TOTAL FOR YEAR / TICKETS SOLD for each movie, rounded to 2 decimals).

	  Write this newly created dictionary to a JSON file using the given `output_file` as the JSON file name.
	  Return the newly created dictionary at the end.

	  Structure of the dictionary:

		{<Name of the Movie 1> : {"Average Ticket Price" : <TOTAL FOR YEAR / TICKETS SOLD, rounded to 2 decimals>
												 "Genre" : <Genre of the Movie>,
												  "Year" : <Year the Movie was released>,
								  },
		 <Name of the Movie 2> : {
									...
								  }
		}


	  Tip: Pass in the parameter `indent = 4` into your json method to format the JSON file.

	  Output:

	  { 'Avengers: Endgame': {
							  'Average Ticket Price': 9.16,
							  'Genre': 'N/A',
							  'Year': 2019
							 },
		'Bad Boys For Life': {
							  'Average Ticket Price': 9.16,
							  'Genre': 'N/A',
							  'Year': 2020
							 },
		   'Batman Forever': {
							  'Average Ticket Price': 4.35,
							  'Genre': 'Drama',
							  'Year': 1995
							 },
		...
		etc.
		...
	  }
	"""
	pass

def highest_grossing(cleaned_list):
	'''
3.	Using the cleaned list of lists from question 1, find the difference in total profit in 2019$ 
   	between the top two highest grossing movies. Return a string formatted as:
   	
   	"The highest grossing film, <highest grossing film>, earned $<profit difference> more than <second highest grossing film>."
	
   	Output:
		"The highest grossing film, Titanic, earned $7469806 more than Avengers: Endgame."
	'''
	pass

def indecisive_movie(cleaned_list, output_file):
	'''
4. 	You and your friends are having a movie night, but you keep running into
	problems when it comes to choosing a movie. Your friends have come up with
	a list of criteria that the movie must follow. Manipulate the list according
	to the decided criteria and create a list with only movies that follow the
	criteria. Then sort the acceptable movies based on number of tickets sold from
	highest to lowest.
	Return the final sorted and manipulated list.

		Create a file that describes the movies in the manipulated list using the following format:
		"{Movie Title}, released in {Year}, was produced by {distributer} and grossed ${total in 2019} in 2019 dollars."

	Criteria:
		1.  Movie Distributer must not be Walt Disney or Warner Bros.
		2.  Movie Genre must be either action or adventure
		3.  The year that the movie was released must be even
		4.  The movie cannot be Shrek 2

	Make sure there is a new line between each movie

	'''
	pass

if __name__ == '__main__':
		#### Question 1 #####
	cleaned = read_csv("HighestGrossers.csv")
	pprint(cleaned)

	##### Question 2 #####
	# formated_data = export_json(cleaned, "movie_data.json")
	# pprint(formated_data)

	#### Question 3 #####
	# print(highest_grossing(cleaned))

	#### Question 4 #####
	# pprint(indecisive_movie(cleaned, 'top_five.txt'))