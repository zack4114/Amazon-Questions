# Given an array of positive integers. All numbers occur even number
#  of times except one number which occurs odd number of times. Find the number in O(n) time & constant space.

# Input : arr = {1, 2, 3, 2, 3, 1, 3}
# Output : 3

# Input : arr = {5, 7, 2, 7, 5, 2, 5}
# Output : 5


# Naive approach O(n^2) and constant space complexity
# def findOddElement(listOfNumbers):
# 	for i in listOfNumbers:
# 		count_i = 0
# 		for j in listOfNumbers:
# 			if j == i:
# 				count_i += 1
# 		if count_i %2 == 1:
# 			return i

# listOfNumbers = [1, 2, 3, 2, 3, 1, 3]
# print(findOddElement(listOfNumbers))


# Using hash (count table) O(n) time complexity
# Space complexity is high
# def findOddElement(listOfNumbers):
# 	hashTable = [0] * (max(listOfNumbers)+1)
# 	for i in listOfNumbers:
# 		hashTable[i] += 1
# 	for i in range(len(hashTable)):
# 		if hashTable[i]%2 == 1:
# 			return hashTable[i]
# listOfNumbers = [1, 2, 3, 2, 3, 1, 3]
# print(findOddElement(listOfNumbers))


# Using XOR O(n) timeComplexity and constant space complexity
# The Best Solution is to do bitwise XOR of all the elements. XOR of all elements gives us odd occurring element. 
# Please note that XOR of two elements is 0 if both elements are same and XOR of a number x with 0 is x.

def findOddElement(listOfNumbers):
	result = 0
	for i in listOfNumbers:
		result = result ^ i
	return result
listOfNumbers = [1, 2, 3, 2, 3, 1, 3]
print(findOddElement(listOfNumbers))




