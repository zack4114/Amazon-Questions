# Binary Search Tree | Set 1 (Search and Insertion)
# The following is definition of Binary Search Tree(BST) according to Wikipedia

# Binary Search Tree, is a node-based binary tree data structure which has the following properties:

# The left subtree of a node contains only nodes with keys lesser than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# The left and right subtree each must also be a binary search tree.
# There must be no duplicate nodes.

class Node(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None


def search(root,key):
	if root is None:
		print("not Found")
		return
	if root.data is key:
		print("found")
		return
	elif root.data < key:
		search(root.right,key)
	elif root.data > key:
		search(root.left,key)
def insert(root,x):
	temp = Node(x)
	if root is None:
		root = temp
	else:
		if x < root.data:
			if root.left is None:
				root.left = temp
			else:
				insert(root.left,x)
		else:
			if root.right is None:
				root.right = temp
			else:
				insert(root.right,x)

def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.data)
		inorder(root.right)

root = Node(8)
insert(root,3)
insert(root,10)
insert(root,1)
insert(root,6)
insert(root,14)
insert(root,4)
insert(root,7)
insert(root,13)
# inorder(root)
search(root,19)

