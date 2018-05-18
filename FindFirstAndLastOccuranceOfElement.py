# Given a sorted array with possibly duplicate elements, the task is to find 
# indexes of first and last occurrences of an element x in the given array.

# Input : arr[] = {1, 3, 5, 5, 5, 5 ,67, 123, 125}    
#         x = 5
# Output : First Occurrence = 2
#          Last Occurrence = 5

# Input : arr[] = {1, 3, 5, 5, 5, 5 ,7, 123 ,125 }    
#         x = 7
# Output : First Occurrence = 6
#          Last Occurrence = 6

# O(Logn) SOlution
def findFirstOccurance(listOfNumbers,number):
	start = 0
	end = len(listOfNumbers)
	while(end >= start):
		mid = (end+start)//2
		if(number == listOfNumbers[mid]) and (mid == 0 or listOfNumbers[mid-1] < number):
			return mid
		elif (number <= listOfNumbers[mid]):
			end = mid - 1
		elif (number > listOfNumbers[mid]):
			start = mid + 1
	return -1



def findLastOccurance(listOfNumbers,number):
	start = findFirstOccurance(listOfNumbers,number)
	end = len(listOfNumbers)
	while(end >= start):
		mid = (end+start)//2
		if(number == listOfNumbers[mid]) and (mid == 0 or listOfNumbers[mid+1] > number):
			return mid
		elif (number < listOfNumbers[mid]):
			end = mid - 1
		elif (number >= listOfNumbers[mid]):
			start = mid + 1
	return -1


listOfNumbers = [1, 3, 5, 5, 5, 5 ,67, 123, 125]
print(findFirstOccurance(listOfNumbers,123))
print(findLastOccurance(listOfNumbers,123))



# O(n) Solution

# def findFirstAndLastOccurance(listOfNumbers,number):
# 	result = [-1,-1]
# 	for x in range(len(listOfNumbers)):
# 		if listOfNumbers[x] != number:
# 			continue
# 		if result[0] == -1:
# 			result[0] = x
# 		result[1] = x
# 	return result
# listOfNumbers = [1, 3, 5, 5, 5, 5 ,67, 123, 125]
# print(findFirstAndLastOccurance(listOfNumbers,3))