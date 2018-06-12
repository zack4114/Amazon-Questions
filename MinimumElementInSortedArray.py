# Find the minimum element in a sorted and rotated array
# A sorted array is rotated at some unknown point, find the minimum element in it.

# Following solution assumes that all elements are distinct.

# Examples

# Input: {5, 6, 1, 2, 3, 4}
# Output: 1

# Input: {1, 2, 3, 4}
# Output: 1

# Input: {2, 1}
# Output: 1

# naive approach is to travel linearly and find the minimum element in the array
# import math
# def findMin(l):
# 	m = math.inf
# 	for i in l:
# 		if i < m:
# 			m = i
# 	return m

# print(findMin([5, 6, 1, 2, 3, 4]))

# Since the array is sorted we can use binary search to find the minimum element
# but the binary search method cannot be applicable in case of having duplicates in array like [2,2,2,2,0,2,2,2,2,2,2]
import math
def findMin(l):
	m = math.inf
	start = 0
	end = len(l) - 1
	while(start <= end):
		mid = (start + end)//2
		if l[mid] < m:
			m = l[mid]
			if l[end] > l[mid]:
				end = mid - 1
			else:
				start = mid +1
		elif l[mid] > m:
			start = mid+1
	return m
print(findMin([2, 3, 4, 5, 6, 7, 8, 1]))
