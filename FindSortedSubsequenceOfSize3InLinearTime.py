# Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and i < j < k in 0(n) time. 
# If there are multiple such triplets, then print any one of them.
# Input:  arr[] = {12, 11, 10, 5, 6, 2, 30}
# Output: 5, 6, 30

# Input:  arr[] = {1, 2, 3, 4}
# Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4

# Input:  arr[] = {4, 3, 2, 1}
# Output: No such triplet
import math
def findSubsequence(listOfNumbers):
	firstMin = math.inf
	secondMin = math.inf
	thirdMin = math.inf
	temp = 0
	for i in listOfNumbers:
		if i < firstMin:
			firstMin = i
		elif i < secondMin and i > firstMin:
			temp = firstMin
			secondMin = i
		elif i < thirdMin and i > secondMin:
			thirdMin = i
			print(temp,secondMin,thirdMin)
			return
	print("no triplet")

findSubsequence([6, 7, 1, 8])


