# Given an expression string exp , write a program to examine whether the pairs and the orders of 
# “{“,”}”,”(“,”)”,”[“,”]” are correct in exp. For example, the program should print true for exp = “[()]{}{[()()]()}” 
# and false for exp = “[(])”

def returnP(x):
	if x == '[':
		return ']'
	elif x == '{':
		return '}'
	elif x == '(':
		return ')'

def check(string):
	if len(string) == 0:
		return True
	if len(string)%2 == 1:
		return False
	stack = []
	# stack.append(string[0])
	for i in range(len(string)):
		if len(stack) == 0:
			stack.append(string[i])
		else:
			if returnP(stack[-1]) == (string[i]):
				stack.pop()
			else:
				stack.append(string[i])
	# print(stack)
	if len(stack) == 0:
		return True
	else:
		return False

print(check('{()}[]{{}'))