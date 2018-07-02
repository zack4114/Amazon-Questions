# Given an array A[] and a number x, check for pair in A[] with sum as x
# Write a C program that, given an array A[] of n numbers and another number x, 
# determines whether or not there exist two elements in S whose sum is exactly x.

# one approach is to sort the array O(nlogn)
# iterate the array from both the ends and find the pair
# Time complexity is O(n)
# def findPair(l,s):
# 	l.sort()
# 	left = 0
# 	right = len(l) - 1
# 	while(left < right):
# 		if l[left]+l[right] == s:
# 			print(l[left],l[right])
# 			break
# 		if l[left]+l[right] > s:
# 			right -= 1
# 		if l[left]+l[right] < s:
# 			left += 1
# findPair([1, 4, 45, 6, 10, -8],2)


# Efficient methos is to use hashing in O(n) time complexity
def findPair(l,s):
	h = set()
	for i in l:
		if s - i in h:
			print (s-i,i)
		else:
			h.add(i)
findPair([1, 4, 45, 6, 10, -8],16)