# Given an unsorted array, find the minimum difference between any pair in given array.
# Input  : {1, 5, 3, 19, 18, 25};
# Output : 1
# Minimum difference is between 18 and 19

# Input  : {30, 5, 20, 9};
# Output : 4
# Minimum difference is between 5 and 9

# Input  : {1, 19, -4, 31, 38, 25, 100};
# Output : 5
# Minimum difference is between 1 and -4


# Naive Approach O(n^2)
# import math
# def findMinDiff(listOfNumbers):
# 	diff = math.inf
# 	for i in range(len(listOfNumbers)-1):
# 		for j in range(i+1,len(listOfNumbers)):
# 			if abs(listOfNumbers[j] - listOfNumbers[i]) < diff:
# 				diff = abs(listOfNumbers[j] - listOfNumbers[i])
# 	return diff

# listOfNumbers=[30, 5, 20, 9]
# print(findMinDiff(listOfNumbers))


# O(nlogn) Approach
# The idea is to use sorting. Below are steps.
# 1) Sort array in ascending order. This step takes O(n Log n) time.
# 2) Initialize difference as infinite. This step takes O(1) time.
# 3) Compare all adjacent pairs in sorted array and keep track of minimum difference. This step takes O(n) time.

import math
def findMinDiff(listOfNumbers):
	diff = math.inf
	listOfNumbers.sort()
	for i in range(len(listOfNumbers)-1):
		if abs(listOfNumbers[i+1]-listOfNumbers[i]) < diff:
			diff = abs(listOfNumbers[i+1]-listOfNumbers[i])
	return diff
listOfNumbers=[1, 19, -4, 31, 38, 25, 100]
print(findMinDiff(listOfNumbers))