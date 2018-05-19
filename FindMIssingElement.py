# You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in list. 
# One of the integers is missing in the list. Write an efficient code to find the missing integer.

# Naive solution :
# find sum of natural numbers till list digit of the list and then subtract the elemnts of the list from it 
# The result will be the missing number
# I/P    [1, 2, 4,6, 3, 7, 8]
# O/P    5


# def findMissingElement(listOfNumbers):
# 	lastElement = listOfNumbers[-1]
# 	expectedSum = (lastElement) * (lastElement+1) // 2
# 	Sum = sum(listOfNumbers)
# 	return expectedSum - Sum

# listOfNumbers=[1, 2, 4,6, 3, 7, 8]
# print(findMissingElement(listOfNumbers))


#  Efficient approach using XOR
# let a1,a2,a3,a4,a6 in list missing a5
# xor list elements X1 = a1^a2^a3^a4^a6
# xor till last element X2 = a1^a2^a3^a4^a5^a6
# xor x1 and x2 => (a1^a2^a3^a4^a6)^(a1^a2^a3^a4^a5^a6)
# =>(a1^a1)^a2^a2^a3^a3^a4^a4^a5^a6^a6
# giving a5
# O(n)
# Overflow will never occur in this case

def findMissingElement(listOfNumbers):
	x1 = 0
	x2 = 0
	for x in listOfNumbers:
		x1 = x1^x
	for x in range(1,listOfNumbers[-1]+1):
		x2 = x2^x
	return x2^x1


listOfNumbers=[1, 2, 4,6, 3, 7, 8]
print(findMissingElement(listOfNumbers))