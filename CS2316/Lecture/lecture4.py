#does not put back together, must use join
print(str(list("cat")))
#dictionary 
print(dict([(1,2),(2,3),(2,5)]))
#does not allow an iterable
	#print(dict([1,2,3,4,5,6]))

#conditional
num = -1
num = num if num > 0 else 0
num = 0 if num < 0 else num
print(num)

#sets
mylist = [1,3,4,2,2,1,4,5]
mylist = list(set(mylist))
print(set(mylist))

value = "".join(set(["a","b","a"]))
print(set(["a","b","a"])) #ba or ab

#imports
import math as m
print(m.sqrt(5))

import lecture4module as lec
lec.my_module()

#practice
def record_result(first , second) :
	printer = "Record Broken!" if first < second else "Number remains unchanged"
	print(printer)

print(record_result(2,4))

def count_unique(listing) :
	setList = len(set(listing))
	print(setList)

print(count_unique(["ATL","NYC","ATL"]))

def sort_by_last(namelist)
	return sorted(namelist,key=lambda string:(string.split()[1]))
print(sort_by_last(["Josh Hall", "marylyn Chen", "Zhiyi Li"]))

