#Andrew J Miller
#5/16/17

#This program returns the position of a searched
#item in a list of numbers. 
#I'm not going to allow exceptions for algorithms.

def binary_search(list, item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high) / 2
		guess = list[mid]

		if guess == item:
			return mid

		if guess > item:
			high = mid - 1

		else:
			low = mid + 1
	return None