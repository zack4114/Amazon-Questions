# Number of buildings facing the sun
# Given an array representing heights of buildings. The array has buildings from left to right as shown in below diagram, 
# count number of buildings facing the sunset. It is assumed that heights of all buildings are distinct.

# Input : arr[] = {7, 4, 8, 2, 9}
# Output: 3
# Explanation: As 7 is the first element, it can 
# see the sunset.
# 4 can't see the sunset as 7 is hiding it. 
# 8 can see.
# 2 can't see the sunset.
# 9 also can see the sunset.

# Input : arr[] = {2, 3, 4, 5}
# Output : 4

def findCount(l):
	leftMax = 0
	count = 0
	for i in l:
		if i > leftMax:
			leftMax = i
			count +=1
	return count
print(findCount([2,3,4,5]))
