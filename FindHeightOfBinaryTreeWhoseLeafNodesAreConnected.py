# Find height of a special binary tree whose leaf nodes are connected
# Given a special binary tree whose leaf nodes are connected to form a circular doubly linked list, find its height.

# For example,


#       1 
#     /   \ 
#       2      3 
#     /  \ 
#    4    5
#   /   
#  6 
# In the above binary tree, 6, 5 and 3 are leaf nodes and they form a circular doubly linked list. Here, the 
# left pointer of leaf node will act as a previous pointer of circular doubly linked list and its right pointer 
# will act as next pointer of circular doubly linked list.

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


def isLeafNode(node):
	return (node.left is not None and node.left.right == node and node.right is not None and node.right.left == node)

def height(root):
	if root is None:
		return 0
	if isLeafNode(root):
		return 1
	return 1 + max(height(root.left),height(root.right))


root = node(1)
root.child(2,3)
root.left.child(4,5)
root.left.left.child(6,None)
root.right.left = root.left.right
root.right.right = root.left.left.left
root.left.right.right = root.right
root.left.right.left = root.left.left.left
root.left.left.left.right = root.left.right
root.left.left.left.left = root.right
print(height(root))