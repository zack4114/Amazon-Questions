# A function to convert the list to string given that you encounter '\0' in string 
def toString(buff):
	string = ""
	for x in buff:
		if x == '\0':
			print(string)
			return
		string += x

# Generates the patters for string recursively 
def makePattern(string,buff,stringIndex,bufferIndex,stringLen): 
	if(stringIndex == stringLen):
		buff[bufferIndex] = '\0'
		toString(buff)
		return

	buff[bufferIndex] = string[stringIndex]
	makePattern(string,buff,stringIndex+1,bufferIndex+1,stringLen)

	buff[bufferIndex] = ' '
	buff[bufferIndex+1] = string[stringIndex]
	makePattern(string,buff,stringIndex+1,bufferIndex+2,stringLen)


def generatePattern(string):
	stringLen = len(string)
	buff = [0] * 2*stringLen #a buffer can have maximum length of 2 * length of string , let length of string be 'n', therfore for biggest string no of gaps will be n-1 and one term
							  # character.
	buff[0] = string[0]
	makePattern(string,buff,1,1,stringLen)


string = "12345"
generatePattern(string)

"""Time Complexity as there are n-1 gaps therefore total no of strings with gaps = 2^(n-1) and each pattern have range from n to 2n-1 therefore timecomplexity
 = O(n*(2^n))"""