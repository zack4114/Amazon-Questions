# Find duplicates in O(n) time and O(1) extra space | Set 1
# Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times. 
# Find these repeating numbers in O(n) and using only constant memory space.
# For example, let n be 7 and array be {1, 2, 3, 1, 3, 6, 6,6}, the answer should be 1, 3, 6 and 6.

def findDuplicates(l):
	for i in range(len(l)):
		if l[abs(l[i])] < 0:
			print(abs(l[i]))
		else:
			l[abs(l[i])] = -l[abs(l[i])]
findDuplicates([1, 2, 3, 1, 3, 6, 6,6,6,6])