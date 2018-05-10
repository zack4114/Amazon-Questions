"""Problem: Can string2 can be made from string1 after rotating string1 by certain given number (roationNo)
Approach: A string can be rotated in anticlockwise or in clockwise direction only
		  Case1: Anticlock wise rotation => left shift the string 
		  		 newstring = string[k:] + string[:k]
		  Case2: Clockwise rotation => right shift the string
		  		 newstring = string[len(string) - k :] + string[: len(string) - k]"""



def canMakeAterRotation(string1,string2,rotationNo):
	antiClockString = string1[rotationNo:] + string1[:rotationNo]
	clockString = string1[len(string1) - rotationNo : ] + string1[: len(string1) - rotationNo]

	return antiClockString == string2 or clockString == string2

string1 = "geeks"
string2 = "eksge"
rotationNo = 2

print(canMakeAterRotation(string1,string2,rotationNo))
