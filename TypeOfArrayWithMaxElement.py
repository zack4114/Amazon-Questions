# Type of array and its maximum element
# Given an array, it can be of 4 types
# (a) Ascending
# (b) Descending
# (c) Ascending Rotated
# (d) Descending Rotated
# Find out which kind of array it is and return the maximum of that array.

# Input :  arr[] = { 2, 1, 5, 4, 3}
# Output : Descending rotated with maximum element 5

# Input :  arr[] = { 3, 4, 5, 1, 2}
# Output : Ascending rotated with maximum element 5

# O(n) time Complexity

def typrOfArray(listOfNumbers):
	n = len(listOfNumbers)
	for i in range(n):
		while ( i < n-1 and listOfNumbers[i+1] > listOfNumbers[i] ):
			i += 1
		if i == n - 1:
			print("ascending",listOfNumbers[i])
			return
		if i == 0 :
			while( i < n-1 and listOfNumbers[i+1] < listOfNumbers[i]):
				i+= 1
			if i == n - 1:
				print("descending",listOfNumbers[0])
				return
			elif i < n and listOfNumbers[0] < listOfNumbers[i + 1]:
				print("descending Rotated",max(listOfNumbers[i+1],listOfNumbers[0]))
				return
			else:
				print("ascending Rotated",listOfNumbers[0])
				return
		elif i < n and listOfNumbers[0] > listOfNumbers[i + 1]:
			print('ascending Rotated',max(listOfNumbers[0],listOfNumbers[i]))
			return

		else:
			print("descending Rotated",listOfNumbers[-1])

typrOfArray([4, 5, 6, 1, 2, 3])
typrOfArray([2, 1, 7, 5, 4, 3])
typrOfArray([1, 2, 3, 4, 5, 8])
typrOfArray([9, 5, 4, 3, 2, 1])

