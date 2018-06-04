# Given an array with both +ive and -ive integers, return a pair with highest product.
# Input: arr[] = {1, 4, 3, 6, 7, 0}  
# Output: {6,7}  

# Input: arr[] = {-1, -3, -4, 2, 0, -5} 
# Output: {-4,-5} 


# Naive O(n^2) approach

# def findPair(listOfNumbers):
# 	a = listOfNumbers[0]
# 	b = listOfNumbers[1]
# 	for i in range(len(listOfNumbers)):
# 		for j in range(i+1,len(listOfNumbers)):
# 			if listOfNumbers[i] * listOfNumbers[j] > a * b:
# 				a = listOfNumbers[i]
# 				b =listOfNumbers[j]
# 	print(a,b)

# listOfNumbers=[-1, -3, -4, 2, 0, -5]
# findPair(listOfNumbers)


# Better O(nlogn) approach
# Use sorting and if array has all positive integers then return last two numbers
# If array has negative integers also the compare the product of first 2 and last 2 and return the maximum

# def findPair(listOfNumbers):
# 	listOfNumbers.sort()
# 	if listOfNumbers[0]*listOfNumbers[1] > listOfNumbers[-1]*listOfNumbers[-2]:
# 		print(listOfNumbers[0],listOfNumbers[1])
# 	else:
# 		print(listOfNumbers[-1],listOfNumbers[-2])

# listOfNumbers=[-1, -3, -4, 2, 0, -5]
# findPair(listOfNumbers)





# better approach O(n)
# traverse the array and find four elements max, second max, negative max and second negative max 

def findPair(listOfNumbers):
	maximum = 0
	secondMax = 0
	minimum = 0
	secondMin = 0
	for i in listOfNumbers:
		if i > maximum:
			secondMax = maximum
			maximum = i
		if i < minimum:
			secondMin = minimum
			minimum = i
	# print(maximum,secondMin,minimum,secondMax)
	if maximum * secondMax > minimum*secondMin:
		print(maximum,secondMax)
	else:
		print(minimum,secondMin)
listOfNumbers=[-1, -3, -4, 2, 0, -5]
findPair(listOfNumbers)