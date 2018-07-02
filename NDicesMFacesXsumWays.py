# Dynamic Programming | Set 30 (Dice Throw)
# Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. X is 
# the summation of values on each face when all the dice are thrown.

# This problem can be efficiently solved using Dynamic Programming (DP).

# Let the function to find X from n dice is: Sum(m, n, X)
# The function can be represented as:
# Sum(m, n, X) = Finding Sum (X - 1) from (n - 1) dice plus 1 from nth dice
#                + Finding Sum (X - 2) from (n - 1) dice plus 2 from nth dice
#                + Finding Sum (X - 3) from (n - 1) dice plus 3 from nth dice
#                   ...................................................
#                   ...................................................
#                   ...................................................
#               + Finding Sum (X - m) from (n - 1) dice plus m from nth dice

# So we can recursively write Sum(m, n, x) as following
# Sum(m, n, X) = Sum(m, n - 1, X - 1) + 
#                Sum(m, n - 1, X - 2) +
#                .................... + 
#                Sum(m, n - 1, X - m)

def findWays(n,m,x):
	table = [[0]*(x+1) for i in range(n+1)]
	for i in range(1,x+1):
		if i <= m:
			table[1][i] = 1

	for i in range(2,n+1):
		for j in range(1,x+1):
			for k in range(1,j):
				if k <= m:
					table[i][j] += table[i-1][j-k]

	print(table[n][x])
	print(table)
findWays(3,6,8)

