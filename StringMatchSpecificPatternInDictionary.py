# Given a dictionary of words, find all strings that matches the given pattern where every character in the pattern 
# is uniquely mapped to a character in the dictionary.

# Input:  
# dict = ["abb", "abc", "xyz", "xyy"];
# pattern = "foo"
# Output: [xyy abb]
# Explanation: 
# xyy and abb have same character at index 1 and 2 like the pattern

# Input:  
# dict = ["abb", "abc", "xyz", "xyy"];
# pat = "mno"
# Output: [abc xyz]
# Explanation: 
# abc and xyz have all distinct characters, similar to the pattern

# Input:  
# dict = ["abb", "abc", "xyz", "xyy"];
# pattern = "aba"
# Output: [] 
# Explanation: 
# Pattern has same character at index 0 and 2. 
# No word in dictionary follows the pattern.

# Input:  
# dict = ["abab", "aba", "xyz", "xyx"];
# pattern = "aba"
# Output: [aba xyx]
# Explanation: 
# aba and xyx have same character at index 0 and 2 like the pattern


# Idea is to use hash and store the pattern of occurance of the letters in the given pattern string and then generate the hash for 
# all the other strings and compare that hash with the pattern string hash 
# timecomplexity O(total characters in dictionary)
def findHash(string):
	h = {}
	res = ""
	count = 0
	for ch in string:
		if ch not in h.keys():
			h[ch] = count
			count += 1
		res += str(h[ch])
	return res

def findStrings(listOfStrings,pattern):
	patternLen = len(pattern)
	patternHash = findHash(pattern)
	for string in listOfStrings:
		if patternLen == len(string) and patternHash == findHash(string):
			print(string,end = " ")
listOfStrings=["bab", "abc", "xyz", "xyy"]
pattern = "foo"
findStrings(listOfStrings,pattern)
print()






