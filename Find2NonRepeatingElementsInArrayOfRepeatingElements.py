# Find the two non-repeating elements in an array of repeating elements
# Asked by SG
# Given an array in which all numbers except two are repeated once. (i.e. we have 2n+2 numbers and n numbers are occurring 
# twice and remaining two have occurred once). Find those two numbers in the most efficient way.

# arr[] = {2, 4, 7, 9, 2, 4}
# O/P = 7,9


# Naive approach is to sort the array and then just check the adjecent element return the elements which are appearing more
# than once
# Time complexity will be O(nLogn)

# def findRepeatingElements(l):
# 	l.sort()
# 	for i in range(len(l)):
# 		if i == 0 and l[i] != l[i+1]:
# 			print(l[i])
# 		elif i == len(l) - 1 and l[i] != l[i-1]:
# 			print(l[i])
# 		elif l[i] != l[i-1] and l[i] != l[i+1]:
# 			print(l[i])
# findRepeatingElements([2,4,7,9,2,4])
# print()


# Using XOR in O(n)
def findRepeatingElements(l):
	x = 0
	y = 0
	xor = 0
	for i in l:
		xor ^= i
	rightMostBit = xor & (-xor)
	for i in l:
		if i & rightMostBit:
			x ^= i
		else:
			y ^= i
	print(x,y)
findRepeatingElements([2,4,7,9,2,4])
