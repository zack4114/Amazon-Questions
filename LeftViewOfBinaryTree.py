# Print Left View of a Binary Tree
# Given a Binary Tree, print left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited 
# from left side.

# Input : 
#                  1
#                /   \
#               2     3
#              / \     \
#             4   5     6             
# Output : 1 2 4

# Input :
#         1
#       /   \
#     2       3
#       \   
#         4  
#           \
#             5
#              \
#                6
# Output :1 2 4 5 6

# we need to print the left boundary of the binary tree
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
def printLeftBoundary(root):
	if root is None:
		return
	else:
		print(root.data,'->',end='')
		if (root.left is None):
			printLeftBoundary(root.right)
		printLeftBoundary(root.left)


root = node(1)
root.child(2,3)
root.left.child(None,4)
root.left.right.child(None,5)
root.left.right.right.child(None,6)
printLeftBoundary(root)
