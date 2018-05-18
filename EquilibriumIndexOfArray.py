# Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum 
# of elements at higher indexes. For example, in an arrya A:

# A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0

# 3 is an equilibrium index, because:
# A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

# 6 is also an equilibrium index, because sum of zero elements is zero, i.e., A[0] + A[1] + A[2] + A[3] + 
# A[4] + A[5]=0

# 7 is not an equilibrium index, because it is not a valid index of array A.

# Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n, returns 
# an equilibrium index (if any) or -1 if no equilibrium indexes exist.


# Naive Approach
# O(n^2)
# def findEquilibriumIndex(listOfNumbers):
# 	result = []
# 	# print(listOfNumbers)
# 	for i in range(1,len(listOfNumbers)-1):
# 		if sum(listOfNumbers[:i]) == sum(listOfNumbers[i+1:]):
# 			result.append(i)
# 	if sum(listOfNumbers[1:]) == 0:
# 		result.append(0)
# 	if sum(listOfNumbers[:len(listOfNumbers)-1]) == 0:
# 		result.append(len(listOfNumbers)-1)
# 	return result

# listOfNumbers = [-7,1,5,2,-4,3,0]
# print(findEquilibriumIndex(listOfNumbers))


# Efficient Approach O(n)
# The idea is to get total sum of array first. Then Iterate through the array and keep updating the left 
# sum which is initialized as zero. In the loop, we can get right sum by subtracting the elements one by one.

def findEquilibriumIndex(listOfNumbers):
	rightSum = sum(listOfNumbers)
	leftSum = 0
	result = []
	for i in range(len(listOfNumbers)):
		rightSum = rightSum-listOfNumbers[i]
		if leftSum == rightSum:
			result.append(i)
		leftSum += listOfNumbers[i]
	return result

listOfNumbers = [-7,1,5,2,-4,3,0]
print(findEquilibriumIndex(listOfNumbers))



