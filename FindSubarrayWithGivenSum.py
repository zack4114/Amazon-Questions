# Find subarray with given sum | Set 1 (Nonnegative Numbers)
# Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.

# Examples :

# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Ouptut: Sum found between indexes 2 and 4

# Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
# Ouptut: Sum found between indexes 1 and 4

# Input: arr[] = {1, 4}, sum = 0
# O/P "no subarray found"


# Naive Solution to run two loop first loop for starting element of subarray and then next loop for finding the subarray
# Worst case time complexity is O(n^2)

# def findSubarray(l,s):
# 	n = len(l)
# 	for i in range(n):
# 		SUM = 0
# 		for j in range(i,n):
# 			SUM += l[j]
# 			if SUM is s:
# 				print("Sum found between",i,"and",j)
# 				return
# 	print("No Subarray Found")
# findSubarray([1,4],0)


# Efficient Approach
# Initialize a variable curr_sum as first element. curr_sum indicates the sum of current subarray. Start 
# from the second element and add all elements one by one to the curr_sum. If curr_sum becomes equal to sum, 
# then print the solution. If curr_sum exceeds the sum, then remove trailing elements while curr_sum is greater than sum.

# Time comlexity is O(n)
def findSubarray(l,s):
	n = len(l)
	start = 0
	curr_sum = 0
	for i in range(n):
		while(curr_sum > s and start < i-1):
			curr_sum -= l[start]
			start += 1

		if curr_sum == s:
			print("sum found between",start,"and",i-1)
			return
		if i < n:
			curr_sum += l[i]
	print("No subarray found")

findSubarray([1,4,0,0,3,10,5],7)


