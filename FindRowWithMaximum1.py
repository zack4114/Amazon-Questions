# Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.

# Example
# Input matrix
# 0 1 1 1
# 0 0 1 1
# 1 1 1 1  // this row has maximum 1s
# 0 0 0 0

# Output: 2

# simple solutions is to use two loops and store the return the max count of 1s
# O(m*n)
# def findCount(l):
# 	res= 0
# 	temp = 0
# 	for i in range(len(l)):
# 		count = 0
# 		for j in l[i]:
# 			if j == 1:
# 				count+=1
# 		if count > temp:
# 			res = i
# 			temp = count
# 	return res
# l = [[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
# print(findCount(l))

# efficient approach is to find the index of 1st one in each row, row with least index is the row with max 1s
# to find the index of first occurance of 1 we can use binary search
# time complexity will be (mlogn)
# def findCount(l):
# 	res = 0
# 	count = len(l)
# 	n = len(l)
# 	for i in range(n):
# 		start = 0
# 		end = len(l[i]) - 1
# 		while(start <= end):
# 			mid = (start+end)//2
# 			if l[i][mid] == 1 and (mid == 0 or l[i][mid-1]  == 0):
# 				if mid < count:
# 					count = mid
# 					res = i
# 				break
# 			elif l[i][mid] == 1 and l[i][mid-1] == 1:
# 				end = mid - 1
# 			elif l[i][mid] == 0:
# 				start = mid + 1
# 	return res
# l = [[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
# print(findCount(l))



# another efficient appraoch in O(m+n)
# Step1: Get the index of first (or leftmost) 1 in the first row.

# Step2: Do following for every row after the first row
# …IF the element on left of previous leftmost 1 is 0, ignore this row.
# …ELSE Move left until a 0 is found. Update the leftmost index to this index and max_row_index to be the current row.

# The time complexity is O(m+n) because we can possibly go as far left as we came ahead in the first step.

def findRow(l):
	res = 0
	n = len(l)
	fi = len(l[0]) - 1
	for i in range(len(l[0])):
		if l[0][i] == 1:
			fi = i
			break
	for i in range(1,n):
		if l[i][fi - 1] == 0:
			continue
		else:
			while(l[i][fi - 1] == 1 and fi > 0):
				res = i
				fi -= 1
	return res
l = [[0,1,1,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
print(findRow(l))





