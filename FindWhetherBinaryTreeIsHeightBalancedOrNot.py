# A tree where no leaf is much farther away from the root than any other leaf. Different balancing schemes allow different 
# definitions of “much farther” and different amounts of work to keep them balanced.

# Consider a height-balancing scheme where following conditions should be checked to determine if a binary tree is balanced.
# An empty tree is height-balanced. A non-empty binary tree T is balanced if:
# 1) Left subtree of T is balanced
# 2) Right subtree of T is balanced
# 3) The difference between heights of left subtree and right subtree is not more than 1.


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

def height(root):
	if root is None:
		return 0
	else:
		return max(height(root.left),height(root.right))+1

def isBalancedTree(root):
	if root is None:
		return 1
	lh = height(root.left)
	rh = height(root.right)
	if (abs(lh-rh) <= 1 and isBalancedTree(root.left) and isBalancedTree(root.right)):
		return 1
	return 0


root = node(1)
root.child(2,3)
root.left.child(4,5)
root.right.child(8,9)
root.left.left.child(6,7)
print("balanced") if isBalancedTree(root) else print("not balanced")