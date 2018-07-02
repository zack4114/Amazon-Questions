# Given a Binary Tree where each node has positive and negative values. Convert this to a tree where each node 
# contains the sum of the left and right sub trees in the original tree. The values of leaf nodes are changed to 0.

# For example, the following tree

#                   10
#                /      \
#              -2        6
#            /   \      /  \ 
#          8     -4    7    5
# should be changed to

#                  20(4-2+12+6)
#                /      \
#           4(8-4)      12(7+5)
#            /   \      /  \ 
#          0      0    0    0

class Tree(object):
  def __init__(self,x):
    self.data = x
    self.left = None
    self.right = None
  def child(self,lx,rx):
    if lx is not None:
      self.left = Tree(lx)
    if rx is not None:
      self.right = Tree(rx)

def inorderTraversal(root):
  if root is not None:
    inorderTraversal(root.left)
    print(root.data)
    inorderTraversal(root.right)

def isLeafNode(root):
  if root is None:
    return False
  elif root.left is None and root.right is None:
    return True
  return False

def convertToSumTree(root):
  if root is None:
    return 0
  else:
    oldVal = root.data
    root.data = convertToSumTree(root.left) + convertToSumTree(root.right)
    return root.data+oldVal

root = Tree(10)
root.child(-2,6)
root.left.child(8,-4)
root.right.child(7,5)
inorderTraversal(root)
convertToSumTree(root)
print()
inorderTraversal(root)
