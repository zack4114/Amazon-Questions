# Find the two repeating elements in a given array
# You are given an array of n+2 elements. All elements of the array are in range 1 to n. And all elements occur once except 
# two numbers which occur twice. Find the two repeating numbers.

# For example, array = {4, 2, 4, 5, 2, 3, 1} and n = 5

# The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice. So the output 
# should be 4 2.

# Naive approach is to use two loops and count the number of ocurance of each digit
# O(n^2)
# def findElement(l):
# 	for i in range(len(l)):
# 		for j in range(i+1,len(l)):
# 			if l[i] == l[j]:
# 				print(l[i])
# findElement([4,2,4,5,2,3,1])

# Better approach is to use count array which stores the count of each number
# O(n) time complexity and O(n) space complexity
# def findElement(l):
# 	count = [0] * (len(l)-1)
# 	for i in range(len(l)):
# 		count[l[i]] += 1
# 	for i in range(len(count)):
# 		if count[i] == 2:
# 			print(i)
# findElement([4,2,4,5,2,3,1])

# Better approach using XOR in O(n) time complexity and O(1) space complexity
# This method is only applicable when there are only two elments that have only 1 repeatition
# Let the repeating numbers be X and Y, if we xor all the elements in the array and all integers from 1 to n, 
# then the result is X xor Y.
# The 1’s in binary representation of X xor Y is corresponding to the different bits between X and Y. 
# Suppose that the kth bit of X xor Y is 1, we can xor all the elements in the array and all integers from 1 to n, 
# whose kth bits are 1. 
# The result will be one of X and Y. 
# def findElements(l):
# 	x = 0
# 	y = 0
# 	xor = 0
# 	for i in l:
# 		xor ^= i
# 	for i in range(1,len(l) - 1 ):
# 		xor ^= i
# 	rightMostBit = xor & (-xor)
# 	for i in l:
# 		if i & rightMostBit:
# 			x ^= i
# 		else:
# 			y ^= i
# 	for i in range(1,len(l) - 1):
# 		if i & rightMostBit:
# 			x ^= i
# 		else:
# 			y ^= i
# 	print(x,y)
# 	return
# findElements([4,2,4,5,5,3,1])


# Another approach in O(n) time complexity and O(1) space complexity but is only applicable for the arrays having non
 # negative numbers
# beware this will change your original array
def findElements(l):
	for i in range(len(l)):
		if l[abs(l[i])] < 0:
			print(abs(l[i]))
		else:
			l[abs(l[i])] = -l[abs(l[i])]
findElements([4,2,4,5,5,3,1])


