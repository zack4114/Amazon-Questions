# # Write a Program to Find the Maximum Depth or Height of a Tree
# # Given a binary tree, find height of it. Height of empty tree is 0 and height of below tree is 3.
# 						1
# 				2				3
# 			4		5

class Tree(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None
	def child(self,lx,rx):
		if lx is not None:
			self.left = Tree(lx)
		if rx is not None:
			self.right = Tree(rx)


def findHeight(root):
	if root is None:
		return 0
	else:
		ld = findHeight(root.left)
		rd = findHeight(root.right)
		return (max(ld,rd) + 1)
root = Tree(1)
root.child(2,3)
root.left.child(4,5)
root.left.left.child(4,5)
print(findHeight(root))