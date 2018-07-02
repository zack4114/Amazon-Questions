# Tree Isomorphism Problem
# Write a function to detect if two trees are isomorphic. Two trees are called isomorphic if one of them can be obtained 
# from other by a series of flips, i.e. by swapping left and right children of a number of nodes. Any number of nodes at 
# any level can have their children swapped. Two empty trees are isomorphic.
# We simultaneously traverse both trees. Let the current internal nodes of two trees being traversed be n1 and n2 
# respectively. There are following two conditions for subtrees rooted with n1 and n2 to be isomorphic.
# 1) Data of n1 and n2 is same.
# 2) One of the following two is true for children of n1 and n2
# ……a) Left child of n1 is isomorphic to left child of n2 and right child of n1 is isomorphic to right child of n2.
# ……b) Left child of n1 is isomorphic to right child of n2 and right child of n1 is isomorphic to left child of n2.


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

def areIsoMorphic(root1,root2):
	 if root1 is None and root2 is None:
	 	return True
	 if root1 is None or root2 is None:
	 	return False
	 if root1.data != root2.data:
	 	return False
	 return ((areIsoMorphic(root1.left,root2.left) and areIsoMorphic(root1.right,root2.right))or(areIsoMorphic(root1.left,root2.right) and areIsoMorphic(root1.right,root2.left)))

def inoder(root):
	if root is not None:
		inoder(root.left)
		print(root.data)
		inoder(root.right)

root1 = node(1)
root1.child(2,3)
root1.left.child(4,5)
root1.right.child(6,None)
root1.left.right.child(7,8)


root2 = node(1)
root2.child(3,2)
root2.left.child(None,6)
root2.right.child(4,5)
root2.right.right.child(8,7)
# print(inoder(root1))
# print()
# print(inoder(root2))
# print()
print(areIsoMorphic(root1,root2))