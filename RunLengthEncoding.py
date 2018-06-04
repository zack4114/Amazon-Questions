# Given an input string, write a function that returns the Run Length Encoded string for the input string.

# For example, if the input string is “wwwwaaadexxxxxxaaa”, then the function should return “w4a3d1e1x6”.


def runLengthEncoding(string):
	result = ''
	result += string[0]
	count = 1
	temp = string[0]
	for i in range(1,len(string)):
		if temp == string[i]:
			count += 1
		else:
			result += str(count)
			temp = string[i]
			count = 1
			result += temp
	result+=str(count)
	print(result)

string = 'wwwwaaadexxxxxxax'
runLengthEncoding(string)