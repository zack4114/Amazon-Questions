# Find index of an extra element present in one sorted array
# Given two sorted arrays. There is only 1 difference between the arrays. First array has one element extra 
# added in between. Find the index of the extra element.

# Input : {2, 4, 6, 8, 9, 10, 12};
#         {2, 4, 6, 8, 10, 12};
# Output : 4
# The first array has an extra element 9.
# The extra element is present at index 4.

# Input :  {3, 5, 7, 9, 11, 13}
#          {3, 5, 7, 11, 13}
# Output :  3


# Naive approach O(n) math each number in both the arrays if the number doesnt match return the number and the index

# def findMismatch(l1,l2):
# 	for i in range(len(l2)):
# 		if l1[i] is not l2[i]:
# 			return (i,)


# l1 = [2, 4, 6, 8, 9, 10, 12]
# l2 = [2, 4, 6, 8, 10, 12]
# print(findMismatch(l1,l2))


# O(logn) approach using binary search 
# math the mid element in both the arrays if the mid element is similar than serach for the mismatch element in the right 
# side of the array
# is the mismatch occur than do the binary search in left subarray to find the firs mismatch index

def findMismatch(l1,l2):
	res = -1
	start = 0
	end = len(l2) - 1
	while(start<=end):
		mid = (start+end)//2
		if l1[mid] == l2[mid]:
			start = mid+1
		else:
			res = mid
			end = mid - 1
	return res

l1 = [3, 5, 7, 9, 11, 13]
l2 = [3, 5, 7, 11, 13]
print(findMismatch(l1,l2))
