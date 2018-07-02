# Check if a given Binary Tree is SumTree
# Write a function that returns true if the given Binary Tree is SumTree else false. A SumTree is a Binary Tree 
# where the value of a node is equal to sum of the nodes present in its left subtree and right subtree. An empty 
# tree is SumTree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.

# Following is an example of SumTree.

#           26
#         /   \
#       10     3
#     /    \     \
#   4      6      3

# The time complexity of this method is O(n^2) since we are visiting each node twice 
# once while traversing and another while calculating the sum using getsum method

class Tree(object):
	def __init__(self,x):
		self.left = None
		self.right = None
		self.data = x

	def child(self,lx,rx):
		if lx is not None:
			self.left = Tree(lx)
		if rx is not None:	
			self.right = Tree(rx)

# def getsum(root):
# 	if root == None:
# 		return 0
# 	return getsum(root.left) + root.data + getsum(root.right)
# def isSumTree(root):
# 	ls = 0
# 	rs = 0
# 	if (root == None or (root.left == None and root.right==None)):
# 		return 1
# 	ls = getsum(root.left)
# 	rs = getsum(root.right)
# 	if (root.data==ls+rs and isSumTree(root.left) and isSumTree(root.right)):
# 		return 1
# 	return 0


# root = Tree()
# root.data = 10
# root.left = Tree()
# root.right = Tree()
# root.left.data = 4
# root.right.data = 7
# print(isSumTree(root))




# Method 2 ( Tricky ) 
# The Method 1 uses sum() to get the sum of nodes in left and right subtrees. The method 2 uses following rules to get the 
# sum directly.
# 1) If the node is a leaf node then sum of subtree rooted with this node is equal to value of this node.
# 2) If the node is not a leaf node then sum of subtree rooted with this node is twice the value of this node (Assuming 
# that the tree rooted with this node is SumTree).
# Time Complexity is O(n)


def isLeafNode(root):
	if root == None:
		return False
	if root.left == None and root.right == None:
		return True
	return False

def isSumTree(root):
	if root == None or isLeafNode(root):
		return True
	if(isSumTree(root.left) and isSumTree(root.right)):
		ls = 0
		rs = 0
		if root.left == None:
			ls = 0
		elif isLeafNode(root.left):
			ls = root.left.data
		else:
			ls = 2*root.left.data

		if root.right == None:
			rs = 0
		elif isLeafNode(root.right):
			rs = root.right.data
		else:
			rs = 2*root.right.data

		if (root.data == ls+rs):
			return True
		return False
	return False

root = Tree(26)
root.child(10,3)
root.left.child(4,1)
root.right.child(None,3)
print(isSumTree(root))

















