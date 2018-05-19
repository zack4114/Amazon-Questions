# Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers 
# in the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should 
# return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.

# Input : arr[] = {5, 5, 10, 100, 10, 5}
# Output : 110

# Input : arr[] = {1, 2, 3}
# Output : 4

# Input : arr[] = {1, 20, 3}
# Output : 20

# Loop through all the elements:
# make two sum containers
# inclusive => sum till now including current number
# exclusive => summ til now excluding current number
# These sum are in such way that no two elements are adjecent to each other

# O(n) time complexity

def findMaxSum(listOfNumbers):
	inclusive = 0
	exclusive = 0
	for i in listOfNumbers:
		temp = inclusive
		inclusive = exclusive + i   # sum = sum till now excluding previous digit plus current number
		exclusive = max(temp,exclusive)  # sum = sum till now including previous digit and excluding current digit

	return max(inclusive,exclusive)

listOfNumbers = [5, 5, 10, 40, 50, 35]
print(findMaxSum(listOfNumbers))