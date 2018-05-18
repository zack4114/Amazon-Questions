# # Given an array of n distinct integers sorted in ascending order, write a function that returns a Fixed Point 
# # in the array, if there is any Fixed Point present in array, else returns -1. Fixed Point in an array is an 
# # index i such that arr[i] is equal to i. Note that integers in array can be negative.

#   Input: arr[] = {-10, -5, 0, 3, 7}
#   Output: 3  // arr[3] == 3 

#   Input: arr[] = {0, 2, 5, 8, 17}
#   Output: 0  // arr[0] == 0 


#   Input: arr[] = {-10, -5, 3, 4, 7, 9}
#   Output: -1  // No Fixed Point

# Linear Search O(n) Solutions
# def findFixedPoint(listOfNumbers):
# 	result = []
# 	for i in range(len(listOfNumbers)):
# 		if listOfNumbers[i] == i:
# 			result.append(i)
# 	return result

# listOfNumbers=[-10,-5,0,3,7]
# print(findFixedPoint(listOfNumbers))


# Binary Search O(logn) Solutions

def binarySearch(listOfNumbers,start,end):
	if(start <= end):
		mid = (start+end)//2
		if(mid == listOfNumbers[mid]):
			return mid
		elif (listOfNumbers[mid] < mid):
			return binarySearch(listOfNumbers,mid+1,end)
		elif (listOfNumbers[mid] > mid):
			return binarySearch(listOfNumbers,start,mid-1)
	else:
		return -1

def findFixedPoint(listOfNumbers):
	start = 0
	end = len(listOfNumbers)-1
	result = binarySearch(listOfNumbers,start,end)
	return result

listOfNumbers=[-10,-5,0,3,7]
print(findFixedPoint(listOfNumbers))



	