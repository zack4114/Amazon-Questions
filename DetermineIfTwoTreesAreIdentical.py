# Write Code to Determine if Two Trees are Identical
# Two trees are identical when they have same data and arrangement of data is also same.

# To identify if two trees are identical, we need to traverse both trees simultaneously, and while traversing we need 
# to compare data and children of the trees.


# sameTree(tree1, tree2)
# 1. If both trees are empty then return 1.
# 2. Else If both trees are non -empty
#      (a) Check data of the root nodes (tree1->data ==  tree2->data)
#      (b) Check left subtrees recursively  i.e., call sameTree( 
#           tree1->left_subtree, tree2->left_subtree)
#      (c) Check right subtrees recursively  i.e., call sameTree( 
#           tree1->right_subtree, tree2->right_subtree)
#      (d) If a,b and c are true then return 1.
# 3  Else return 0 (one is empty and other is not)

# another approach can be that find inorder+preorder traversal of bothtree or inorder+postordertraversal of both tree if 
# thes are same then the trees are identical


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

# 1st method
# def areIdentical(tree1,tree2):
# 	if tree1 is None and tree2 is None:
# 		return 1
# 	elif tree1 is not None and tree2 is not None:
# 		return(tree1.data is tree2.data and areIdentical(tree1.left,tree2.left) and areIdentical(tree1.right,tree2.right))
# 	else:
# 		return 0


# 2nd method
def inorderTraversal(root,l):
	if root is not None:
		inorderTraversal(root.left,l)
		l.append(root.data)
		inorderTraversal(root.right,l)
def postOrderTraversal(root,l):
	if root is not None:
		postOrderTraversal(root.left,l)
		postOrderTraversal(root.right,l)
		l.append(root.data)
def areIdentical(tree1,tree2):
	lt1 = []
	lt2 = []
	inorderTraversal(tree1,lt1)
	postOrderTraversal(tree1,lt1)
	inorderTraversal(tree2,lt2)
	postOrderTraversal(tree2,lt2)
	print(lt1)
	print(lt2)
	if lt2 == lt1:
		print("true")
	else:
		print("false")



tree1 = node(1)
tree1.child(2,3)
tree1.left.child(4,5)
tree1.right.child(6,7)
tree1.left.left.child(8,9)
tree2 = node(1)
tree2.child(2,3)
tree2.left.child(10,5)
tree2.right.child(6,7)
tree2.left.left.child(8,9)
print(areIdentical(tree1,tree2))
