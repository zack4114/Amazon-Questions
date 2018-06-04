# # Find four elements a, b, c and d in an array such that a+b = c+d
# # Given an array of distinct integers, find if there are two pairs (a, b) and (c, d) such that a+b = c+d, and a, b, c 
# # and d are distinct elements. If there are multiple answers, then print any of them.

# Input:   {3, 4, 7, 1, 2, 9, 8}
# Output:  (3, 8) and (4, 7)
# Explanation: 3+8 = 4+7

# Input:   {3, 4, 7, 1, 12, 9};
# Output:  (4, 12) and (7, 9)
# Explanation: 4+12 = 7+9

# Input:  {65, 30, 7, 90, 1, 9, 8};
# Output:  No pairs found


# Naive approach using four for loops 
def findPairs(listOfNumbers):
	n = len(listOfNumbers)
	for i in range(n-3):
		for j in range(i+1,n-2):
			for k in range(j+1,n-1):
				for l in range(k+1,n):
					if listOfNumbers[i]+listOfNumbers[j] == listOfNumbers[k]+listOfNumbers[l]:
						print("(",listOfNumbers[i],listOfNumbers[j],")",end=" ")
						print("(",listOfNumbers[k],listOfNumbers[l],")")
						print()
	# print("No Pairs")

findPairs([3, 4, 7, 1, 2, 9, 8])