# Floor in a Sorted Array
# Given a sorted array and a value x, the floor of x is the largest element in array smaller than or equal to x. 
# Write efficient functions to find floor of x.

# Examples:

# Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
# Output : 2
# 2 is the largest element in arr[] smaller than 5.

# Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 20
# Output : 19
# 19 is the largest element in arr[] smaller than 20.

# Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 0
# Output : -1
# Since floor doesn't exist, output is -1.

# Naive approach is to do linear search
# find the first number greater than or equal to the given number and then return the number before it 
# # Time Complexity O(n)
# def findFloor(l,x):
# 	if x < l[0]:
# 		return -1
# 	if x >= l[-1]:
# 		return l[-1]
# 	for i in range(len(l)):
# 		if l[i] > x:
# 			return l[i-1]
# print(findFloor([1,2,8,10,10,12,19],20))


# Efficient approach is to use the binary search and find the number which is greater than or equal to the given number
# and return the element just befor it
# Time complexity O(logn)
def findFloor(l,x):
	if x < l[0]:
		print(-1)
		return
	if x >= l[-1]:
		print(l[-1])		
		return 
	start = 0
	end = len(l) - 1
	ans = -1
	while(start <= end):
		mid = (start+end)//2
		if l[mid] >= x and l[mid-1] < x: 
			if l[mid] == x:
				ans = x
			else:
				ans = l[mid - 1]
			break
		elif l[mid] < x:
			start = mid + 1
		else:
			end = mid - 1
	print(ans)
	
findFloor([1,2,8,10,10,12,19],5)
