# Remove minimum number of characters so that two strings become anagram
# Input : str1 = "bcadeh" str2 = "hea"
# Output: 3
# We need to remove b, c and d from str1.

# Input : str1 = "cddgk" str2 = "gcd"
# Output: 2

# Input : str1 = "bca" str2 = "acb"
# Output: 0

# O(m+n) solution
# import collections
# def removeCharacters(string1,string2):
# 	total = 0
# 	alphabet = 'abcdefghijklmnopqrstuvwxyz'
# 	hash_string1 = {}
# 	hash_string2 = {}
# 	hash_string1 = collections.defaultdict(lambda: 0,hash_string1)
# 	hash_string2 = collections.defaultdict(lambda: 0,hash_string2)

# 	for i in string1:
# 		hash_string1[i] += 1
# 	for i in string2:
# 		hash_string2[i] += 1

# 	for i in alphabet:
# 		total += abs(hash_string1.get(i,0) - hash_string2.get(i,0))
# 	return total

# string1 = "abchea"
# string2 = "hea"
# print(removeCharacters(string1,string2))



# Reducing to single hash table 
def removeCharacters(string1,string2):
	total = 0
	hashTable = [0]*26
	for i in string1:
		hashTable[ord(i) - 97] += 1
	for i in string2:
		hashTable[ord(i) - 97] -= 1
	for i in range(26):
		total += abs(hashTable[i])

	return total

string1 = "abchea"
string2 = "hea"
print(removeCharacters(string1,string2))
