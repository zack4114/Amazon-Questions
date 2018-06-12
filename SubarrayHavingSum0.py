# Find the largest subarray with 0 sum
# Given an array of integers, find length of the largest subarray with sum equals to 0.

# Examples:

# Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
# Output: 5
# The largest subarray with 0 sum is -2, 2, -8, 1, 7

# Input: arr[] = {1, 2, 3}
# Output: 0
# There is no subarray with 0 sum

# Input: arr[] = {1, 0, 3}
# Output: 1

# Naive solution run two loops and check for each subarray if sum equal to 0
# O(n^2)
# def findSubarray(l):
# 	n = len(l)
# 	max_length = -1
# 	for i in range(n):
# 		curr_sum = 0
# 		for j in range(i,n):
# 			curr_sum += l[j]
# 			if curr_sum == 0:
# 				max_length = max(max_length,j-i+1)
# 	if max_length == -1:
# 		print("no subarray with sum 0")
# 		return
# 	print(max_length)

# findSubarray([1,31,1,-1,-1,1])




# Efficient solution using hashing in O(n) time complexity and O(n) space complexity
def findSubarray(l):
	n = len(l)
	max_length = -1
	h = {}
	curr_sum = 0
	for i in range(n):
		curr_sum += l[i]
		if l[i] == 0 and max_length == -1:
			max_length = 1
		if curr_sum == 0:
			max_length = i+1
		index = h.get(curr_sum,-1)
		if index != -1:
			max_length = max(max_length,i-h[curr_sum])
		else:
			h[curr_sum] = i
	print(max_length)
findSubarray([15, -2, 2, -8, 1, 7, 10, 23])

