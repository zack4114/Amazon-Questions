# # Given an array of 0s and 1s, in how many iterations the whole array can be filled with 1s if in a single iteration immediate neighbors of 1s can be filled.

# NOTE: If we cannot fill array with 1s, then print “-1” .

# Input : arr[] = {1, 0, 1, 0, 0, 1, 0, 1, 
#                      1, 0, 1, 1, 0, 0, 1}
# Output : 1
# To convert the whole array into 1s, one iteration
# is required. Between indexes i=2 and i=5, the zero 
# at i=3 would be converted to '1' due to its neighbours
# at i=2 similarly the zero at i=4 would be converted 
# into '1' due to its neighbor at i=5, all this can 
# be done in a single iteration. Similarly all 0's can
# be converted to 1 in single iteration.

# Input : arr[] = {0, 0, 1, 1, 0, 0, 1, 1, 0, 
#                     1, 1, 1, 1, 0, 0, 0, 1}
# Output : 2


# My approach O(n) different question

# def checkAllOnes(listOfNumbers):
# 	for x in listOfNumbers:
# 		if x is not 1:
# 			return False
# 	return True
# def countIterations(listOfNumbers):
# 	result = 1
# 	if checkAllOnes(listOfNumbers):
# 		return 0
# 	for x in range(len(listOfNumbers)):
# 		if x == 0:
# 			if listOfNumbers[x] == 1:
# 				listOfNumbers[x+1] = 1
# 		elif(x > 0 and x < len(listOfNumbers)-1):
# 			if listOfNumbers[x] == 1:
# 				listOfNumbers[x-1] = 1
# 				listOfNumbers[x+1] = 1
# 		elif (x == len(listOfNumbers)-1):
# 			if listOfNumbers[x] == 1:
# 				listOfNumbers[x-1] = 1
# 		if x>0:
# 			if listOfNumbers[x-1] == 0 or listOfNumbers[x] == 0:
# 				result += 1
# 	if result >= len(listOfNumbers):
# 		return -1
# 	else:
# 		return result

# listOfNumbers=[1,1,1,1,1,1,1,1]
# print(countIterations(listOfNumbers))



# SOlution O(n) \\


# It is given that a single 1 can convert both its 0 neighbours to 1. This problem boils down to three cases :

# Case 1 : A block of 0s has 1s on both sides

# Let count_zero be the count of zeros in the block.

# Number of iterations are always equal to : 
#               count_zero/2   if (count_zero is even)
#               count_zero+1)/2    if(count_zero is odd).

# Case 2 : Either single 1 at the end or in 
#          the starting. For example 0 0 0 0 1 and 
#          1 0 0 0 0
# In this case the number of iterations required will 
# always be equal to number of zeros.

# Case 3 : There are no 1s (Array has only 0s)
# In this case array can't be filled with all 1's. 
# So print -1.



def countIterations(listOfNumbers):
	result = 0
	oneFound = False
	i = 0
	currentCount = 0
	while(i < len(listOfNumbers)):
		if listOfNumbers[i] == 1:
			oneFound = True

		while(i<len(listOfNumbers) and listOfNumbers[i] == 1):
			i += 1


		zeroCount = 0
		while(i<len(listOfNumbers) and listOfNumbers[i] == 0):
			i += 1
			zeroCount += 1

		if(not oneFound and i==len(listOfNumbers)):
			return -1
		elif (oneFound and i < len(listOfNumbers)):
			if zeroCount%2 == 0:
				currentCount = zeroCount//2
			else:
				currentCount = (zeroCount+1)//2
			zeroCount = 0
		else:
			currentCount = zeroCount
			zeroCount = 0

		result = max(result,currentCount)
		i+=1

	return result


listOfNumbers=[1,1,1,1,1,1,0,0,0,0,1]
print(countIterations(listOfNumbers))






