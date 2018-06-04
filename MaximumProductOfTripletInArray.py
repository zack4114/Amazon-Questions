# Maximum product of a triplet (subsequnece of size 3) in array
# Given an integer array, find a maximum product of a triplet in array.

# Input:  [10, 3, 5, 6, 20]
# Output: 1200
# Multiplication of 10, 6 and 20
 
# Input:  [-10, -3, -5, -6, -20]
# Output: -90

# Input:  [1, -4, 3, -6, 7, 0]
# Output: 168

# Naive approach using three loops o(n^3)
# import math
# def findMaxProduct(l):
# 	n = len(l)
# 	product = -math.inf
# 	for i in range(n-2):
# 		for j in range(i+1,n-1):
# 			for k in range(j+1,n):
# 				product = max(product,l[i]*l[j]*l[k])
# 	return product
# print(findMaxProduct([-10, -3, -5, -6, -20]))


# Using Sorting method O(nlogn):
# def findMaxProduct(l):
# 	l.sort()
# 	return max(l[0]*l[1]*l[2],l[-1]*l[-2]*l[-3])
# print(findMaxProduct([-10, -3, -5, -6, -20]))


# by finding first three minimun and first three maximum in O(n) and the return the max of the product of the two
import math
def findMaxProduct(l):
	firstMax = -math.inf
	secondMax = -math.inf
	thirdMax = -math.inf
	firstMin = math.inf
	secondMin = math.inf
	thirdMin = math.inf
	for i in l:
		if i > firstMax:
			thirdMax = secondMax
			secondMax = firstMax
			firstMax = i
		elif i > secondMax:
			thirdMax = secondMax
			secondMax = i
		elif i > thirdMax:
			thirdMax = i
		if i < firstMin:
			thirdMin = secondMin
			secondMin = firstMin
			firstMin = i
		elif i < secondMin:
			thirdMin = secondMin
			secondMin = i
		elif i < thirdMin:
			thirdMin = i
	return max(firstMin*secondMin*thirdMin,firstMax*secondMax*thirdMax)

print(findMaxProduct([10, 3, 5, 6, 20]))