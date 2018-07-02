# Extract Leaves of a Binary Tree in a Doubly Linked List
# Given a Binary Tree, extract all leaves of it in a Doubly Linked List (DLL). Note that the DLL need to be created 
# in-place. Assume that the node structure of DLL and Binary Tree is same, only the meaning of left and right pointers 
# are different. In DLL, left means previous pointer and right means next pointer.

# Let the following be input binary tree
#         1
#      /     \
#     2       3
#    / \       \
#   4   5       6
#  / \         / \
# 7   8       9   10


# Output:
# Doubly Linked List
# 7<->8<->5<->9<->10

# Modified Tree:
#         1
#      /     \
#     2       3
#    /         \
#   4           6


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

def inoder(root):
  if root is not None:
    inoder(root.left)
    print(root.data,end=" ")
    inoder(root.right)

def isLeafNode(root):
  if root is None:
    return False
  if root.left is None and root.right is None:
    return True
  return False

def printLinkedList(root):
  while(root is not None):
    print(root.data,"<->",end=" ")
    root = root.right

def removeLeafNodes(root):
  global DLL
  global temp
  if root is None:
    return None
  if isLeafNode(root):
    if DLL is None:
      DLL = root
      temp = DLL
    else:
      temp.right = root
      root.left = temp
      temp = temp.right 
    # del(root)
    return None
  root.left = removeLeafNodes(root.left)
  root.right = removeLeafNodes(root.right)
  return root

root = node(1)
root.child(2,3)
root.left.child(4,5)
root.left.left.child(7,8)
root.right.child(None,6)
root.right.right.child(9,10)
DLL = None
temp = None
inoder(root)
print()
removeLeafNodes(root)
print()
inoder(root)
print()
printLinkedList(DLL)
print()

