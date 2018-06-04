# Remove characters from the first string which are present in the second string

# O(m+n) solution

import collections
def removeCharacters(string1,string2):
	string2Hash = {}
	string2Hash = collections.defaultdict(lambda:0,string2Hash)
	result = ''
	for i in string2:
		string2Hash[i] = 1
	for i in string1:
		if string2Hash.get(i,-1) == -1:
			result += i
	return result

string1 = "geeksforgeeks"
string2 = "mask"
print(removeCharacters(string1,string2))