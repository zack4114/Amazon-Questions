# Given a Binary Tree, print all nodes that don’t have a sibling (a sibling is a node that has same parent. 
# In a Binary Tree, there can be at most one sibling). Root should not be printed as root cannot have a sibling.

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

def findNodes(root):
	if root is None:
		return
	if root.left is None and root.right is not None:
		print(root.right.data)
	elif root.left is not None and root.right is None:
		print(root.left.data)
	findNodes(root.left)
	findNodes(root.right)

root = Tree(1)
root.child(2,None)
root.left.child(None,4)
findNodes(root)
