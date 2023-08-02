def showToWatch(friendsfavshows, favoriteshow) :
	a = []
	for item in friendsfavshows :
		if favoriteshow in item[1] :
			a.append(item[0])
	print(a)



friendsfavshows = [('Eric', ['Friends', 'B99']), ('Anthony' , ['Money Heist', 'Friends']) , ('Sara' , ['Friends','Elite'])]
favoriteshow = 'Friends'
showToWatch(friendsfavshows,favoriteshow)