# Count all possible paths from top left to bottom right of a mXn matrix
# The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that 
# from each cell you can either move only to right or down

# We can use recursive programming to find the total number of paths
# But in this approach the time complexity is exponential

# def findNumberOFPaths(m,n):
# 	if m is 1 or n is 1:
# 		return 1

# 	return findNumberOFPaths(m-1,n) + findNumberOFPaths(m,n-1)+findNumberOFPaths(m-1,n-1)
# 	 # m-1 for 1 movement downwards
# 	 # n-1 for one movement rightwards
# print(findNumberOFPaths(2,3)) 


# Better approach is to use dynamic programming
def findNumberOfPaths(m,n):
	count = [[0]*n for i in range(n)]
	# count of path to element in first row
	for i in range(n):
		count[0][i] = 1
	# Count of path to element in first column
	for i in range(m):
		count[i][0] = 1
	for i in range(1,m):
		for j in range(1,n):
			count[i][j] = count[i-1][j]+count[i][j-1]+count[i-1][j-1]
	return count[m-1][n-1]
print(findNumberOfPaths(2,3))