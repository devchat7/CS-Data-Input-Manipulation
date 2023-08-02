#join
def get_string(alist) :
	return "-".join(alist)

a_tuple = (False, 1, 2.0, 'three', ['four'])
new_tuple = a_tuple + (3,)
print(new_tuple)
print(a_tuple[-1])

a_dict = {'key1' : 'val1', 'key2' : 'val2'}
b_dict = {'key2' : 'val2', 'key1' : 'val1'}
print(a_dict == b_dict)
print(a_dict)
print(4%3)

c_dict = {}  # empty dictionary
c_dict['key2' , 'val1'] = "val3"
print(c_dict)

atl = ('ATL', 'Braves')
miami = ('Miami', 'Marlins')

mapping = dict([atl,miami])
print(mapping)

print(get_string(["Yellow", "Jacket", "Baseball"]))

pixar = "PIXAR"
for index , each_char in enumerate(pixar): 
	pass

pixar = ["P","I","X","A","R"]
pixar_string = "".join(pixar)
print(pixar_string)

def get_string(abc, string2) :
	print(abc)
	print(string2)


print(get_string("hello" , "string"))


#Tuple
data = ('George P. Burdell' , 92, 'ISyE')
name, lister, major = data
students = [data, data, data]
print(students)
print(lister)

def sort_sublist(list1) :
	for index in list1 :
		index.sort()
	return list1


#Lists
	#sort changes the list
	#sorted makes a completely new list
	#reverse can be used in both
def sort_sublists(alist):
	for item in alist:
		item.sort()
alist= [[1,2],[5,3],[6,2]]
sort_sublists(alist)
print(alist)

#Dictionary
num1 = [1,2,6,2,4,8]
num2 = (4,5,1,2,3,4)
d = {}
for pos in range(len(num1)): # 0 1 2 3 4 5
	d[num1[pos]] = num2[pos]
print(d) 

for item in d:
	print(item) #gives the keys and not the values

d = {}
for num in [.5,.7,.9]:
    d[int(num)] = num
print(d)

#create_d practice

list1 = [1, 2, 3, 4]
list2 = ["one", "two", "three", "four"]

def create_d(list1, list2):
	return dict(zip(list1 , list2))

print(create_d(list1, list2))

#sort_names practice

sortList = ["John Smith", "Melinda McDaniel", "Deven Chatterjea"]

def sort_names(sortList):
	return sorted(sortList, key = lambda name: name.split()[-1]) #Creates lists within the lists

print(sort_names(sortList))

def letter_counts(string1) :
	dict1 = dict(string1)