# Find the maximum repeating number in O(n) time and O(1) extra space


# Given an array of size n, the array contains numbers in range from 0 to k-1 where k is a positive integer and k <= n. 
# Find the maximum repeating number in this array. For example, let k be 10 the given array be 
# arr[] = {1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3}, the maximum repeating number would be 2. 
# Expected time complexity is O(n) and extra space allowed is O(1). Modifications to array are allowed.


# Naive appraoch to use two loops which count the occurance of each number in O(n^2)
# def findMaxCount(l):
# 	number = -1
# 	max_count = 0
# 	for i in l:
# 		count = 0
# 		for j in l:
# 			if i == j:
# 				count += 1
# 		if count > max_count:
# 			max_count = count
# 			number = i
# 	return number
# print(findMaxCount([1, 3, 3, 3, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3]))

# better approach to use count sort 
# time complexity = O(n)
# space complexity = O(k) k = max element in array
# since range of the array is (0 to k-1) and k<=n
# def findMaxCount(l):
# 	n = len(l)
# 	h = [0]*n
# 	res = 0
# 	for i in range(n):
# 		h[l[i]] += 1
# 	for i in range(n):
# 		if h[i] > res:
# 			res = i
# 	return res
# print(findMaxCount([1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3]))





# Efficient approach 
# using the array itself as the hash 
# since all the numbers in the array are less than the range of the array then there will be no conflicts
# O(n) time complexity and O(1) space complexity
# Consider array  arr[] = {2, 3, 3, 5, 3, 4, 1, 7}
# 1) Iterate though input array arr[], for every element arr[i], increment arr[arr[i]%k] by k (arr[] becomes 
# 	{2, 11, 11, 29, 11, 12, 1, 15 })

# 2) Find the maximum value in the modified array (maximum value is 29). Index of the maximum value is the maximum 
# repeating element (index of 29 is 3).

# 3) If we want to get the original array back, we can iterate through the array one more time and do 
# arr[i] = arr[i] % k where i varies from 0 to n-1.

def findMaxCount(l):
	n = len(l)
	for i in range(n):
		l[l[i]%n] += n
	res = 0
	temp = 0
	for i in range(n):
		if l[i] > temp:
			temp = l[i]
			res = i
	return res
print(findMaxCount([2, 3, 3, 5, 3, 4, 1, 7])) 


