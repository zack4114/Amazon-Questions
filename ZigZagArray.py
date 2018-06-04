# /# Given an array of distinct elements, rearrange the elements of array in zig-zag fashion 
# in O(n) time. The converted array should be in form a < b > c < d > e < f.

# Example: 
# Input:  arr[] = {4, 3, 7, 8, 6, 2, 1}
# Output: arr[] = {3, 7, 4, 8, 2, 6, 1}

# Input:  arr[] =  {1, 4, 3, 2}
# Output: arr[] =  {1, 4, 2, 3}


def zigzag(listOfNumbers):
	for i in range(len(listOfNumbers)-1):
		if i %2 == 0:
			if listOfNumbers[i] > listOfNumbers[i+1]:
				listOfNumbers[i],listOfNumbers[i+1] = listOfNumbers[i+1],listOfNumbers[i]
		else:
			if listOfNumbers[i] < listOfNumbers[i+1]:
				listOfNumbers[i],listOfNumbers[i+1] = listOfNumbers[i+1],listOfNumbers[i]

	print(listOfNumbers)

zigzag([1, 4, 3, 2])