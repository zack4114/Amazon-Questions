# Find the Rotation Count in Rotated Sorted array
# Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. 
# Given such an array, find the value of k.

# Examples:

# Input : arr[] = {15, 18, 2, 3, 6, 12}
# Output: 2
# Explanation : Initial array must be {2, 3,
# 6, 12, 15, 18}. We get the given array after 
# rotating the initial array twice.

# Input : arr[] = {7, 9, 11, 12, 5}
# Output: 4

# Input: arr[] = {7, 9, 11, 12, 15};
# Output: 0

# Ifwe observe in this then we will find that the number of rotations the array has been done is equal to the idenx of the
# minimum element in the array 
# So the problem reduces to find the minimum element in the sorted array

# Naive approach find the minimum element index in the array using linear search in O(n)
import math
# def findNumberOfRotations(l):
# 	m = math.inf
# 	n = len(l)
# 	index = 0
# 	for i in range(n):
# 		if l[i] < m:
# 			m = l[i]
# 			index = i
# 	return index

# efficient approach to find the minimum element using the binary search in O(logn)
def findNumberOfRotations(l):
	start = 0
	end = len(l) - 1
	m = math.inf
	index = 0
	while(start <= end):
		mid = (start+end)//2
		if l[mid] < m:
			m = l[mid]
			index = mid
			if l[end] > l[mid]:
				end = mid - 1
			else:
				start = mid + 1
		else:
			start = mid + 1
	return index
print(findNumberOfRotations([7,9,11,12,5]))

