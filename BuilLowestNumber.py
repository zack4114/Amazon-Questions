# Build Lowest Number by Removing n digits from a given number
# Given a string ‘str’ of digits and an integer ‘n’, build the lowest possible number by removing ‘n’ digits from the string and not changing the order of input digits.

# Input: str = "4325043", n = 3
# Output: "2043"

# Input: str = "765028321", n = 5
# Output: "0221"

# Input: str = "121198", n = 2
# Output: "1118" 

# The idea is based on the fact that a character among first (n+1) characters must be there in resultant number.
# So we pick the smallest of first (n+1) digits and put it in result, and recur for remaining characters

def buildLowestNumber(inputString,inputNo,result):
	if inputNo == 0:
		result.extend(inputString)
		return result

	if len(inputString) < inputNo:
		result.extend(inputString)		# print("HELLOW")
		return result
	else:
		temp = inputString[:inputNo+1]
		result.append(min(temp))
		minIndex = temp.index(min(temp))
		inputString = inputString[minIndex+1:]
		buildLowestNumber(inputString,inputNo - minIndex,result)


inputString = "765028321"
inputNo = 5
result = []
temp = list(inputString)
temp = [int(x) for x in temp]
buildLowestNumber(temp,inputNo,result)
result = [str(x) for x in result]
result = ''.join(result)
print(result)


# time Complexity = O(n)