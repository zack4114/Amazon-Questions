# A permutation, also called an “arrangement number” or “order,” is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.
# Below are the permutations of string ABC.
# ABC ACB BAC BCA CBA CAB

# can be done using backtracking in O(n*n!)

def permute(string,start,end):
	if start == end:
		print(''.join(string))
		return
	else:
		for i in range(start,end+1):
			string[start],string[i] = string[i],string[start]
			# print(''.join(string))
			permute(string,start+1,end)
			string[start],string[i] = string[i],string[start]

string = "ABC"
string = list(string)
permute(string,0,len(string)-1,)