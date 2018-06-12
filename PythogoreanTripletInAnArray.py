# Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

# Example:

# Input: arr[] = {3, 1, 4, 6, 5}
# Output: True
# There is a Pythagorean triplet (3, 4, 5).

# Input: arr[] = {10, 4, 6, 12, 5}
# Output: False
# There is no Pythagorean triplet.


# Naive O(n^3) solution simply using three loops to find the pythogorean triplet
# def findTriplet(l):
# 	n = len(l)
# 	for i in range(n):
# 		for j in range(n):
# 			for k in range(n):
# 				if l[i]**2 == l[j]**2 + l[k]**2:
# 					print(l[i],l[j],l[k])
# 					return
# 	print("There is no Pythagorean Triplet")
# findTriplet([3,1,4,6,5])


# Efficient solution in O(n^2)
# Using sorting
# first square the array elements
# then sort the squared array elements
# the take the last element of the array and find the pair btw first element and the last element such that there exist a
# pair whose sum is equal to the last element 
# if there is no such pair then take the second last element and search for pair 
import math
def findTriplet(l):
	l = [x**2 for x in l]   #O(n)
	l.sort() #O(nlogn)
	n = len(l)
	# O(n^2)
	for i in range(n-1,1,-1):
		j = 0
		k = i-1
		while(j<k):
			if l[j]+l[k] == l[i]:
				print("TRUE",math.sqrt(l[i]),math.sqrt(l[j]),math.sqrt(l[k]))
				return
			elif l[j]+l[k] < l[i]:
				j+=1
			elif l[j]+l[k] > l[i]:
				k-=1
findTriplet([3,1,4,6,5])