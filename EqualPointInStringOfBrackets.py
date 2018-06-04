# Find an equal point in a string of brackets

# Given a string of brackets, the task is to find an index k which decides the number of opening brackets is 
# equal to the number of closing brackets.

# String must be consists of only opening and closing brackets i.e. ‘(‘ and ‘)’.

# An equal point is an index such that the number of opening brackets before it is equal 
# to the number of closing brackets from and after.

# Input : str = "(())))("
# Output:   4
# After index 4, string splits into (())
# and ))(. Number of opening brackets in the 
# first part is equal to number of closing 
# brackets in the second part.

# Input : str = "))"
# Output: 2
# As after 2nd position i.e. )) and "empty"
# string will be split into these two parts:
# So, in this number of opening brackets i.e.
# 0 in the first part is equal to number of 
# closing brackets in the second part i.e. 
# also 0.

def findIndex(string):
	if ')' not in string:
		print(0)
		return
	elif '(' not in string:
		print(len(string))
		return
	fromStart = [0]*len(string)
	fromEnd = [0]*len(string)
	count = 0
	for i in range(len(string)):
		if string[i] == '(':
			count += 1
		fromStart[i] = count
	count = 0
	for i in range(len(string)-1,-1,-1):
		if string[i] == ')':
			count += 1
		fromEnd[i] = count
	# print(fromStart)
	# print(fromEnd)
	for i in range(len(fromStart)):
		if fromStart[i] == fromEnd[i]:
			print(i)
			return

findIndex("(((()")