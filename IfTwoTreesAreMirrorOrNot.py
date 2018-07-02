# Check if two trees are Mirror
# Given two Binary Trees, write a function that returns true if two trees are mirror of each other, else false. 
# For example, the function should return true for following input trees.

# 		# 				1								1
# 		# 			3		2						2		3
# 		# 				5		4				4		5

# For two trees ‘a’ and ‘b’ to be mirror images, the following three conditions must be true:

# Their root node’s key must be same
# Left subtree of root of ‘a’ and right subtree root of ‘b’ are mirror.
# Right subtree of ‘a’ and left subtree of ‘b’ are mirror.

# Time COmplexity is O(n)

class Tree(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None

def isMirror(root1,root2):
	if root2 == None and root1 == None:
		return True 
	elif root1 == None or root2 == None:
		return False
	else:
		return root1.data == root2.data and isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left)


root1 = Tree(1)
root1.left = Tree(3)
root1.right = Tree(2)
root1.right.left = Tree(5)
root1.right.right = Tree(4)

root2 = Tree(1)
root2.left = Tree(2)
root2.right = Tree(3)
root2.left.right = Tree(5)
root2.left.left = Tree(4)

print(isMirror(root1,root2))