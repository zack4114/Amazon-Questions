# Given an array of n words. Some words are repeated twice, we need count such words.
# Examples

# Input : s[] = {"hate", "love", "peace", "love", 
#                "peace", "hate", "love", "peace", 
#                "love", "peace"};
# Output : 1
# There is only one word "hate" that appears twice

# Input : s[] = {"Om", "Om", "Shankar", "Tripathi", 
#                 "Tom", "Jerry", "Jerry"};
# Output : 2
# There are two words "Om" and "Jerry" that appear
# twice.

# two method 
# either use count function
# or create a dictionary and store count for each string.

# 1st method: O(n^2)
# def countWords(listOfWords):
# 	result = 0
# 	for x in set(listOfWords):
# 		if listOfWords.count(x) == 2:
# 			result += 1
# 	return result

# listOfWords = ["hate", "love", "peace", "love","peace", "hate", "love", "peace","love", "peace"]
# print(countWords(listOfWords))



# 2nd method O(n)
import collections
def countWords(listOfWords):
	result = 0
	wordDictionary = {}
	wordDictionary = collections.defaultdict(lambda: 0, wordDictionary)
	for x in listOfWords:
		wordDictionary[x] += 1

	for x in wordDictionary.keys():
		if wordDictionary[x] == 2:
			result += 1
	return result

listOfWords = ["hate", "love", "peace", "love","peace", "hate", "love", "peace","love", "peace"]
print(countWords(listOfWords))



