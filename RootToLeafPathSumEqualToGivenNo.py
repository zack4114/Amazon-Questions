# Root to leaf path sum equal to a given number
# Given a binary tree and a number, return true if the tree has a root-to-leaf path such that adding 
# # up all the values along the path equals the given number. Return false if no such path can be found.


# 												10
# 											  /    \
# 											 8      2
# 											/ \    /
# 										   3   5  2


# For example, in the above tree root to leaf paths exist with following sums.

# 21 –> 10 – 8 – 3
# 23 –> 10 – 8 – 5
# 14 –> 10 – 2 – 2

# So the returned value should be true only for numbers 21, 23 and 14. For any other number, returned 
# value should be false.

class node(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None
	def child(self,lx,rx):
		if lx is not None:
			self.left = node(lx)
		if rx is not None:
			self.right = node(rx)
def isLeafNode(root):
	if root is None:
		return False
	elif root.left is None and root.right is None:
		return True
	return False

def findPath(root,s):
	if root is None:
		return False
	if isLeafNode(root) and s-root.data == 0:
		return True
	return findPath(root.left,s-root.data) or findPath(root.right,s-root.data)

root = node(10)
root.child(8,2)
root.left.child(3,5)
root.right.child(2,None)
print(findPath(root,14))






