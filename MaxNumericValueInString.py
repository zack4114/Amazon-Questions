# Given an alphanumeric string, extract maximum numeric value from that string. Alphabets will only be in lower case.
# Input : 100klh564abc365bg
# Output : 564
# Maximum numeric value among 100, 564 
# and 365 is 564.

# Input : abchsd0sdhs
# Output : 0

def findMaxVal(string):
	num = 0
	maxVal = 0
	for i in string:
		if i >= '0' and i <= '9':
			num = num*10 + int(i)
		else:
			maxVal = max(maxVal,num)
			num = 0
	return maxVal

print(findMaxVal("abchsd0sdhs"))