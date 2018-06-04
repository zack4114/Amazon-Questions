# Given an interval, the task is to count numbers which have same first and last digits. For example, \
# 1231 has same first and last digits.

# approach
# we know that all 1 digit numbers have same first digit and last digit
# and after 10 in a interval span of 10 there is only one digit which have same first digit and last digit
# From 120 to 130, only 121 has same starting and ending digit
# From 440 to 450, only 444 has same starting and ending digit
# From 1050 to 1060, only 1051 has same starting and ending digit

def getFirstdigit(n):
	while(n>10):
		n = n//10
	# print(n)
	return n
def countNumbers(n):
	# if n < 10 then numbers having same firt digit and same last digit will be n
	if n < 10:
		return n
	# else we get the number of spans each having 1 number with same first digit and same last digit by dividing n//10
	# and then we add 9 to it to count those single digit numbers
	else:
		count = (n//10) + 9
		# if the last digit is smaller than the first digit of a number then that interval span is not included therefore -1 from ans
		if getFirstdigit(n) > (n%10):
			count -= 1
		return count

# print(countNumbers(7))
# print(countNumbers(68))

print(countNumbers(40) - countNumbers(5)+1) # + 1 is done here because in this method both are inclusive but then we need
											# to include both the numbers therefore in subtraction we exclude that number thats why. add 1
