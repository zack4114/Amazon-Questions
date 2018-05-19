# Find and print the uncommon characters of the two given strings in sorted order. Here uncommon character means that either
# the character is present in one string or it is present in other string but not in both. The strings contain only lowercase 
# characters and can contain duplicates.

# Input : str1 = "characters"
#         str2 = "alphabets"
# Output : b c l p r

# Input : str1 = "geeksforgeeks"
#         str2 = "geeksquiz"
# Output : f i o q r u z

# import collections
# def findUncommonCharacter(string1,string2):
# 	string2Map = {}
# 	string2Map = collections.defaultdict(lambda: 0,string2Map)
# 	string1Map = {}
# 	string1Map = collections.defaultdict(lambda:0,string1Map)
	
# 	# creating hashmap of string 1
# 	for i in string1:
# 		string1Map[i] += 1
	
# 	# creating hashmap for string2
# 	for i in string2:
# 		string2Map[i] += 1

# 	# find string1 characters which are not in string2
# 	for i in string1:
# 		if string2Map.get(i,0) == 0:
# 			print(i,end = ' ')

# 	# find string2 characters which are not in string1
# 	for i in string2:
# 		if string1Map.get(i,0) == 0:
# 			print(i,end=" ")

# string1 = "geeksforgeeks"
# string2 = "geeksquiz"
# findUncommonCharacter(string1,string2)
# print()


# Efficient Solution
#  Use a hash table of size 26 for all the lowercase characters.
# Initially, mark presence of each character as ‘0’ (denoting that the character is not present in both the strings).
# Traverse the 1st string and mark presence of each character of 1st string as ‘1’ (denoting 1st string) in the hash table.
# Now, traverse the 2nd string. For each character of 2nd string, check whether its presence in the hash 
# table is ‘1’ or not. If it is ‘1’, then mark its presence as ‘-1’ (denoting that the character is common to both the 
# strings), else mark its presence as ‘2’ (denoting 2nd string).


def findUncommonCharacters(string1,string2):
	hashTable = {}
	for i in range(26):
		hashTable[i] = 0
	for i in string1:
		hashTable[ord(i) - ord('a')] = 1
	for j in string2:
		if hashTable[ord(j) - ord('a')] == 1 or hashTable[ord(j) - ord('a')] == -1:
			hashTable[ord(j) - ord('a')] = -1
		else:
			hashTable[ord(j) - ord('a')] = 2
	print(hashTable)
	for i in range(26):
		if hashTable[i] == 1 or hashTable[i] == 2:
			print (chr(i+ord('a')),end=' ')

string1 = "geeksforgeeks"
string2 = "geeksquiz"
findUncommonCharacters(string1,string2)
print()




