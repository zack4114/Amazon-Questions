# Given an unsorted array that may contain duplicates. Also given a number k which is smaller than size of array.
 # Write a function that returns true if array contains duplicates within k distance.

 # Input: k = 3, arr[] = {1, 2, 3, 4, 1, 2, 3, 4}
# Output: false
# All duplicates are more than k distance away.

# Input: k = 3, arr[] = {1, 2, 3, 1, 4, 5}
# Output: true
# 1 is repeated at distance 3.

# Input: k = 3, arr[] = {1, 2, 3, 4, 5}
# Output: false

# Input: k = 3, arr[] = {1, 2, 3, 4, 4}
# Output: true
# import collections

# O(n) solutions 
# O(k) auxiliary space
def check(listOfNumbers,k):
	a = set()
	for i in range(len(listOfNumbers)):
		if listOfNumbers[i] in a:
			print("True")
			return
		else:
			if i > k:
				a.pop()
			a.add(listOfNumbers[i])
	print("False")

(check([1, 2, 3, 4, 1, 2, 3, 4],3))