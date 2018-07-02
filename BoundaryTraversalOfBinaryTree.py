# Boundary Traversal of binary tree
# Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root. 
# For example, boundary traversal of the following tree is “20 8 4 10 14 25 22”



# 									20
# 								/		 \				
# 						  	/				\
# 						 /					  \
# 						8						22
# 					  /	   \						  \	
# 					4		12						25		
# 						  /    \
#						10		14




# We break the problem in 3 parts:
# 1. Print the left boundary in top-down manner.
# 2. Print all leaf nodes from left to right, which can again be sub-divided into two sub-parts:
# …..2.1 Print all leaf nodes of left sub-tree from left to right.
# …..2.2 Print all leaf nodes of right subtree from left to right.
# 3. Print the right boundary in bottom-up manner.


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
	else:
		if root.left is None and root.right is None:
			return True
	return False


def printLeftBoundary(root):
	if root is None:
		return
	if root.left is not None:
		print(root.data)
		printLeftBoundary(root.left)
	elif root.right is not None:
		print(root.data)
		printLeftBoundary(root.right)

def printLeafNodes(root):
	if root is not None:
		printLeafNodes(root.left)
		if isLeafNode(root):
			print(root.data)
		printLeafNodes(root.right)

def printRightBoundary(root,head):
	if root is None:
		return
	if root.right is not None:
		printRightBoundary(root.right,head)
		if root is head:
			return
		print(root.data)
	elif root.left is not None:
		printRightBoundary(root.left,head)
		if root is head:
			return
		print(root.data)

root = node(20)
root.child(8,22)
root.left.child(4,12)
root.left.right.child(10,14)
root.right.child(None,22)
root.right.child(None,25)

printLeftBoundary(root)
printLeafNodes(root)
temp = root
printRightBoundary(temp,root)

