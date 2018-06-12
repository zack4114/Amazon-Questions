# Find the maximum element in an array which is first increasing and then decreasing
# Given an array of integers which is initially increasing and then decreasing, find the maximum value in the array.
# Examples :

# Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
# Output: 500

# Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
# Output: 50

# Corner case (No decreasing part)
# Input: arr[] = {10, 20, 30, 40, 50}
# Output: 50

# Corner case (No increasing part)
# Input: arr[] = {120, 100, 80, 20, 0}
# Output: 120

# Naive approach to use linear search and find the element in O(n)
# def findElement(l):
# 	n = len(l)
# 	for i in range(n-1):
# 		if l[i] > l[i+1]:
# 			return l[i]
# 	return l[i+1] #Else return the last element
# print(findElement([8, 10, 20, 80, 100, 200, 400, 500]))


# Efficient approach to use binary search
def findElement(l):
	n = len(l)
	start = 0
	end = n-1
	while start <= end:
		mid = (start+end)//2
		if (mid == 0 or l[mid] > l[mid-1]) and (mid== n-1 or l[mid] > l[mid+1]):
			return l[mid]
		elif l[mid] < l[mid+1]:
			start = mid+1
		elif l[mid] < l[mid-1]:
			end = mid - 1
print(findElement([120, 100, 80, 20, 0]))