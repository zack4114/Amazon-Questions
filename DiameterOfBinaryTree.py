# Diameter of a Binary Tree
# The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes. 
# The diagram below shows two trees each with diameter nine, the leaves that form the ends of a longest path are shaded 
# (note that there is more than one path in each tree of length nine, but no path longer than nine nodes).

# https://cdncontribute.geeksforgeeks.org/wp-content/uploads/Diameter-of-Binary-Tree.png

# The diameter of a tree T is the largest of the following quantities:

# * the diameter of T’s left subtree
# * the diameter of T’s right subtree
# * the longest path between leaves that goes through the root of T (this can be computed from the 
# 	heights of the subtrees of T)


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

def diameter(root):
	if root is None:
		return 0
	else:
		lh = height(root.left)
		rh = height(root.right)
		ld = diameter(root.left)
		rd = diameter(root.right)
		return max(lh+rh+1,max(ld,rd))


root = node(1)
root.child(2,3)
root.left.child(4,5)
print(height(root))
print(diameter(root))