#Andrew J Miller
#5/17/17

#This is a python code for a quicksort recursive algorithm

def quicksort(array):
	if len(array) < 2:
		return array #Because they're literally already sorted.
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]

		return quicksort(less) + [pivot] + quicksort(greater)

#remember to have the output stored in the format:

sortedArray = quicksort(array)