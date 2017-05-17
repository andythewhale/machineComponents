#Andrew J Miller
#5/17/17

#This is a basic python algorithm that sorts a list/array
#The array will automatically sort small --> large
#This is meant to be a skeleton for future development

def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def smallToLargeSorter(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr


#Output should be stored like this:
sorted = smallToLargeSorter(arr)

