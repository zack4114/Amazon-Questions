# Solution
# Following is a 3 step solution for converting Binary tree to Binary Search Tree.
# 1) Create a temp array arr[] that stores inorder traversal of the tree. This step takes O(n) time.
# 2) Sort the temp array arr[]. Time complexity of this step depends upon the sorting algorithm. In the following 
# implementation, Quick Sort is used which takes (n^2) time. This can be done in O(nLogn) time using Heap Sort or 
# Merge Sort.
# 3) Again do inorder traversal of tree and copy array elements to tree nodes one by one. This step takes O(n) time.


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

def inorderTraversal(root):
	if root is not None:
		inorderTraversal(root.left)
		print(root.data)
		inorderTraversal(root.right)

def storeInorder(root,l):
	if root is not None:
		storeInorder(root.left,l)
		l.append(root.data)
		storeInorder(root.right,l)
def insertInoder(root,l):
	if root is not None:
		insertInoder(root.left,l)
		root.data = l[0]
		del(l[0])
		insertInoder(root.right,l)


def BinaryTreeToBST(root):
	l = []
	storeInorder(root,l)
	l.sort()
	insertInoder(root,l)
	inorderTraversal(root)


tree = node(10)
tree.child(2,7)
tree.left.child(8,4)
BinaryTreeToBST(tree)
# l = []
# storeInorder(tree,l)
# inorderTraversal(tree)