# Print Right View of a Binary Tree
# Given a Binary Tree, print Right view of it. Right view of a Binary Tree is set of nodes visible when tree is 
# visited from Right side.

# Right view of following tree is 1 3 7 8

#           1
#        /     \
#      2        3
#    /   \     /  \
#   4     5   6    7
#                   \
#                    8

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

def printRightBoundary(root):
	if root is None:
		return
	else:
		print(root.data,'->',end='')
		if root.right is None:
			printRightBoundary(root.left)
		printRightBoundary(root.right)

root = node(1)
root.child(2,3)
root.left.child(4,5)
root.right.child(6,7)
root.right.right.child(None,8)
printRightBoundary(root)
print()