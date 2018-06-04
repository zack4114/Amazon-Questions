# The atoi() function takes a string (which represents an integer) as an argument and returns its value.

def atoi(string):
	sign = 1
	k = 0
	res = 0
	if string[0] == '-':
		sign = -1
		k = 1
	for i in range(k,len(string)):
		res = res*10 + (ord(string[i]) - ord('0'))
	res = sign*res

	print(res)

atoi('-123124')
