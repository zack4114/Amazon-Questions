# Given an array of integers. Find a peak element in it. An array element is peak if it is NOT smaller than its neighbors. 
# For corner elements, we need to consider only one neighbor. For example, for input array {5, 10, 20, 15}, 20 is the only 
# peak element. For input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and 90. Note that we need to 
# return any one peak element.

# Following corner cases give better idea about the problem.
# 1) If input array is sorted in strictly increasing order, the last element is always a peak element. For example, 50 is 
# peak element in {10, 20, 30, 40, 50}.
# 2) If input array is sorted in strictly decreasing order, the first element is always a peak element. 100 is the peak 
# element in {100, 80, 60, 50, 20}.
# 3) If all elements of input array are same, every element is a peak element


# simple O(n) solution is to iterate the array and check its left and right elements, if the right and left elements are
# smaller then return the element

# def findPeakVal(listOfNumbers):
# 	n = len(listOfNumbers)
# 	for i in range(n):
# 		if i == 0:
# 			if listOfNumbers[i] >= listOfNumbers[i+1]:
# 				return listOfNumbers[i]
# 		elif i == n-1:
# 			if listOfNumbers[i] >= listOfNumbers[i-1]:
# 				return listOfNumbers[i]
# 		else:
# 			if listOfNumbers[i] >= listOfNumbers[i+1] and listOfNumbers[i] >= listOfNumbers[i-1]:
# 				return listOfNumbers[i]

# print(findPeakVal([10,10,10,10,10,10]))


# O(logn) solution using binary search on unsorted array
# if mid element is not smaller than both of its neighbour then return the element
# else if mid element is less than the left element then the peak is in left half , do binary search for left half
# else if mid element is less than the right element then the peak is in right half, do binary search in right half

def findPeakVal(listOfNumbers,start,end):
	if start <= end:
		mid = (start+end)//2
		if (mid == 0):
			if listOfNumbers[mid] >= listOfNumbers[mid+1]:
				return listOfNumbers[mid]
		elif mid == end:
			if listOfNumbers[mid] >= listOfNumbers[mid-1]:
				return listOfNumbers[mid]
		else:
			if listOfNumbers[mid] >= listOfNumbers[mid-1] and listOfNumbers[mid] >= listOfNumbers[mid+1]:
				return listOfNumbers[mid]
		if listOfNumbers[mid] < listOfNumbers[mid-1]:
			return findPeakVal(listOfNumbers,start,mid-1)
		elif listOfNumbers[mid] < listOfNumbers[mid+1]:
			return findPeakVal(listOfNumbers,mid+1,end)

listOfNumbers = [100, 80, 60, 50, 20]
print(findPeakVal(listOfNumbers,0,len(listOfNumbers)-1))
