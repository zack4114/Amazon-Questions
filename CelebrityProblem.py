# The Celebrity Problem
# In a party of N people, only one person is known to everyone. Such a person may be present in the party, 
# if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “. Find 
# the stranger (celebrity) in minimum number of questions.

# We can describe the problem input as an array of numbers/characters representing persons in the party. We 
# also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, false otherwise. 
# How can we solve the problem.

# Method 3 (Using Stack)
# The graph construction takes O(N2) time, it is similar to brute force search. In case of recursion, we reduce the 
# problem instance by not more than one, and also combine step may examine M-1 persons (M – instance size).

# We have following observation based on elimination technique (Refer Polya’s How to Solve It book).

# If A knows B, then A can’t be celebrity. Discard A, and B may be celebrity.
# If A doesn’t know B, then B can’t be celebrity. Discard B, and A may be celebrity.
# Repeat above two steps till we left with only one person.
# Ensure the remained person is celebrity. (Why do we need this step?)
# We can use stack to verity celebrity.

# Push all the celebrities into a stack.
# Pop off top two persons from the stack, discard one person based on return status of HaveAcquaintance(A, B).
# Push the remained person onto stack.
# Repeat step 2 and 3 until only one person remains in the stack.
# Check the remained person in stack doesn’t have acquaintance with anyone else.


def knows(matrix,x,y):
	return matrix[x][y]
def findCeleb(matrix):
	stack = [i for i in range(len(matrix))]
	while(len(stack) > 1):
		x = stack.pop()
		y = stack.pop()
		if knows(matrix,x,y):
			stack.append(y)
		elif knows(matrix,y,x):
			stack.append(x)
	x = stack.pop()
	for i in range(len(matrix)):
		if matrix[x][i] != 0 and matrix[i][x] == 1:
			print("No one is celeb")
			return
	print(x,'is celeb')

matrix = [[0,0,0,0],
		  [0,0,0,0],
		  [1,1,0,1],
		  [0,0,0,0]]
findCeleb(matrix)



