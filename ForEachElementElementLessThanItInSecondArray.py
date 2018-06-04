# Given two unsorted arrays arr1[] and arr2[]. They may contain duplicates. For each element in arr1[] count elements 
# less than or equal to it in array arr2[].

# Input : arr1[] = [1, 2, 3, 4, 7, 9]
        # arr2[] = [0, 1, 2, 1, 1, 4]
        			# [0,1,1,1,1,2,4]
# Output : [4, 5, 5, 6, 6, 6]

# Input : arr1[] = [5, 10, 2, 6, 1, 8, 6, 12]
        # arr2[] = [6, 5, 11, 4, 2, 3, 7]
# Output : [4, 6, 1, 5, 0, 6, 5, 7]

# Naive O(n^2) approach:
# def findResult(l1,l2):
# 	result = [0] * len(l1)
# 	for i in range(len(l1)):
# 		for j in l2:
# 			if j <= l1[i]:
# 				result[i]+=1
# 	print(result)

# findResult([1, 2, 3, 4, 7, 9],[0, 1, 2, 1, 1, 4])


# Efficient Method

def findLastOccurance(l2,n):
	start = 0
	end = len(l2) - 1
	ans = 0
	while(start <= end):
		mid = (start+end)//2
		if (n >= l2[mid] and (mid == 0 or mid == len(l2)-1 or l2[mid+1] > n)):
			ans = mid + 1
			break
		elif (n < l2[mid]):
			end = mid-1
		else:
			start = mid+1
	return ans

def findResult(l1,l2):
	l2.sort()
	result = [0] * len(l1)
	for i in range(len(l1)):
		# print(l1[i])
		result[i] = findLastOccurance(l2,l1[i])
	print(result)
findResult([5, 10, 2, 6, 1, 8, 6, 12],[6, 5, 11, 4, 2, 3, 7])

