# Find the element before which all the elements are smaller than it, and after which all are greater
# Given an array, find an element before which all elements are smaller than it, and after which all are greater than it. 
# Return index of the element if there is such an element, otherwise return -1.

# Examples:

# Input:   arr[] = {5, 1, 4, 3, 6, 8, 10, 7, 9};
# Output:  Index of element is 4
# All elements on left of arr[4] are smaller than it
# and all elements on right are greater.
 
# Input:   arr[] = {5, 1, 4, 4};
# Output:  Index of element is -1
# Expected time complexity is O(n).


# Solution with O(n) time complexity and O(n) space complexity
import math
def findIndex(l):
	n = len(l)
	leftMax = [l[0]]*n
	rightMin = [l[-1]]*n
	for i in range(1,n):
		if l[i] > leftMax[i-1]:
			leftMax[i] = l[i]
		else:
			leftMax[i] = leftMax[i-1]
	for i in range(n-2,-1,-1):
		if l[i] < rightMin[i+1]:
			rightMin[i] = l[i]
		else:
			rightMin[i] = rightMin[i+1]
	print(leftMax,"\n",rightMin)
	for i in range(n):
		if l[i] >= leftMax[i] and l[i] <=rightMin[i]:
			return i
	return -1
print(findIndex([5, 6, 7, 1, 8, 10, 12]))
