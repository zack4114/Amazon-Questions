# A Product Array Puzzle
# Given an array arr[] of n integers, construct a Product Array prod[] (of same size) such that prod[i] is equal 
# to the product of all the elements of arr[] except arr[i]. Solve it without division operator and in O(n).

# Example:
# arr[] = {10, 3, 5, 6, 2}
# prod[] = {180, 600, 360, 300, 900}

# Naive approach  O(n^2)
# def findArray(listOfNumbers):
# 	result = []
# 	for i in range(len(listOfNumbers)):
# 		temp = 1
# 		for j in range(len(listOfNumbers)):
# 			if j is not i:
# 				temp = temp * listOfNumbers[j]
# 		result.append(temp)
# 	print(result)

# findArray([10, 3, 5, 6, 2])

# O(n) approach using division operator
# def findArray(listOfNumbers):
# 	result = []
# 	product = 1
# 	for i in listOfNumbers:
# 		product *= i
# 	for i in listOfNumbers:
# 		result.append(product//i)
# 	print(result)

# findArray([10,3,5,6,2])


# O(n) approach without division operator O(n) auxiliary space complexity and O(n) space complexity

# def findArray(listOfNumbers):
# 	result = []
# 	left = [1] * len(listOfNumbers)
# 	right = [1] * len(listOfNumbers)

# 	for i in range(1,len(listOfNumbers)):
# 		left[i] = left[i-1]*listOfNumbers[i-1]
# 	for i in range(len(listOfNumbers)-2,-1,-1):
# 		right[i] = right[i+1]*listOfNumbers[i+1]
# 	print(left)
# 	print(right)
# 	for i in range(len(listOfNumbers)):
# 		result.append(left[i]*right[i])
# 	print(result)

# findArray([10,3,5,6,2])



# O(n) Time complexity
# O(n) Space Complexity
# O(1) auxiliary space complexity

def findArray(listOfNumbers):
	n = len(listOfNumbers)
	result = [1] * n
	# store left product
	temp = 1
	for i in range(1,n):
		temp *= listOfNumbers[i-1]
		result[i] *= temp

	print(result)

	temp = 1
	for i in range(n-1,-1,-1):
		result[i] *= temp
		temp *= listOfNumbers[i]
	
	print(result)

findArray([10,3,5,6,2])






