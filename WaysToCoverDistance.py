# Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.
# Input:  n = 3
# Output: 4
# Below are the four ways
#  1 step + 1 step + 1 step
#  1 step + 2 step
#  2 step + 1 step
#  3 step

# Input:  n = 4w
# Output: 7

# exponential time using recursion
# def findWays(n):
# 	if n < 0:
# 		return 0
# 	if n == 0:
# 		return 1
# 	return findWays(n-1)+findWays(n-2)+findWays(n-3)

# print(findWays(3))

# in O(n) using Dynamic Programming
def findWays(n):
	a = [0]*(n+1)
	a[0] = 1
	a[1] = 1
	a[2] = 2
	for i in range(3,n+1):
		a[i] = a[i-1]+a[i-2]+a[i-3]
	print(a[-1])
findWays(3)
