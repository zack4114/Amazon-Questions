# Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.

# Examples:

# Input: arr[]   = {2, 0, 2}
# Output: 2
# Structure is like below
# | |
# |_|
# We can trap 2 units of water in the middle gap.

# Input: arr[]   = {3, 0, 0, 2, 0, 4}
# Output: 10
# Structure is like below
#      |
# |    |
# |  | |
# |__|_| 
# We can trap "3*2 units" of water between 3 an 2,
# "1 unit" on top of bar 2 and "3 units" between 2 
# and 4.  See below diagram also.

# Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
#        | 
#    |   || |
# _|_||_||||||
# Trap "1 unit" between first 1 and 2, "4 units" between
# first 2 and 3 and "1 unit" between second last 1 and last 2 
# An element of array can store water if there are higher bars on left and right. We can find amount of water to be 
# stored in every element by finding the heights of bars on left and right sides. The idea is to compute amount of 
# water that can be stored in every element of array. For example, consider the array {3, 0, 0, 2, 0, 4}, we can store 
# two units of water at indexes 1 and 2, and one unit of water at index 2.

# A Simple Solution is to traverse every array element and find the highest bars on left and right sides. Take the smaller 
# of two heights. The difference between smaller height and height of current element is the amount of water that can be 
# stored in this array element. Time complexity of this solution is O(n^2).

def findLeftMax(l):
	lm = [0]*len(l)
	lm[0] = l[0]
	for i in range(1,len(l)):
		lm[i] = max(lm[i-1],l[i])
	return lm
def findRightMax(l):
	rm = [0]*len(l)
	rm[-1] = l[-1]
	for i in range(len(l)-2,-1,-1):
		rm[i] = max(rm[i+1],l[i])
	return rm

def findWaterAmount(l):
	n = len(l)
	lm = findLeftMax(l)
	rm = findRightMax(l)
	amount = 0
	for i in range(len(l)):
		t = min(lm[i],rm[i])-l[i]
		if t >= 0:
			amount += t
	print(amount)



findWaterAmount([3,0,0,2,0,4])







