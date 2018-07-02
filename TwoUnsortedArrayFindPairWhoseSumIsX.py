# Given two unsorted arrays, find all pairs whose sum is x
# Given two unsorted arrays of distinct elements, the task is to find all pairs from both arrays whose sum is equal to x.

# Examples:

# Input :  arr1[] = {-1, -2, 4, -6, 5, 7}
#          arr2[] = {6, 3, 4, 0}  
#          x = 8
# Output : 4 4
#          5 3

# Input : arr1[] = {1, 2, 4, 5, 7} 
#         arr2[] = {5, 6, 3, 4, 8}  
#         x = 9
# Output : 1 8
#          4 5
#          5 4


# Naive approach is to use two loops and find all the pairs whose sum is equal to x
# time complexity is O(n^2) and space complexity is O(1)

# def findPair(l1,l2,x):
# 	for i in l1:
# 		for j in l2:
# 			if i+j is x:
# 				print(i,j)
# l1 = [1, 2, 4, 5, 7]
# l2 = [5, 6, 3, 4, 8]
# x = 9
# findPair(l1,l2,x)

# efficient approach is to use hashing
# time complexity is O(n) and space complexity is O(n)
def findPair(l1,l2,x):
	h = set()
	for i in l1:
		h.add(x-i)
	for i in l2:
		if i in h:
			print(x-i,i)
l1 = [1, 2, 4, 5, 7]
l2 = [5, 6, 3, 4, 8]
x = 9
findPair(l1,l2,x)