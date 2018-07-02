
# Given a number n, write a function that generates and prints all binary numbers with decimal values from 1 to n.

# Examples:

# Input: n = 2
# Output: 1, 10

# Input: n = 5
# Output: 1, 10, 11, 100, 101


# simple way is to run the loop and call dec to bin for every number from 1 to n
# # Time complexity is O(nlogn)
# def dectobin(n):
# 	res = ""
# 	while(n>0):
# 		res += (str(n&1))
# 		n=n>>1
# 	print(res[::-1])
# def findBinary(n):
# 	for i in range(1,n+1):
# 		dectobin(i)
# findBinary(5)


# Another way is to use queue
def findBinary(n):
	q = ["1"]
	while(n>0):
		s = q[0]
		print(s)
		b1 = s
		del(q[0])
		s = s+'0'
		b1 = b1+'1'
		q.append(s)
		q.append(b1)
		n-=1

findBinary(5)



