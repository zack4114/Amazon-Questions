# Print all possible paths from top left to bottom right of a mXn matrix
# The problem is to print all the possible paths from top left to bottom right of a mXn matrix with the constraints that 
# from each cell you can either move only to right or down.

# Examples :

# Input : 1 2 3
#         4 5 6
# Output : 1 4 5 6
#          1 2 5 6
#          1 2 3 6

# Input : 1 2 
#         3 4
# Output : 1 2 4
#          1 3 4
# The algorithm is a simple recursive algorithm, from each cell first print all paths by going down and then print all 
# paths by going right. Do this recursively for each cell encountered.

def prinAllPaths(l,i,j,m,n,path,pi):
	if i == m-1:
		for k in range(j,n):
			path[pi+k-j] = l[i][k]
		print(path[:pi+n-j])
		return
	if j == n -1:
		for k in range(i,m):
			path[pi+k-i] = l[k][j]
		print(path[:pi+m-i])
		return
	path[pi] = l[i][j]
	prinAllPaths(l,i+1,j,m,n,path,pi+1)
	prinAllPaths(l,i,j+1,m,n,path,pi+1)
	prinAllPaths(l,i+1,j+1,m,n,path,pi+1)



l = [[1,2,3],[4,5,6]]
m = len(l)
n = len(l[0])
path = [0]*(m+n-1)
prinAllPaths(l,0,0,m,n,path,0)