# Given only a pointer/reference to a node to be deleted in a singly linked list, how do you delete it?
# A simple solution is to traverse the linked list until you find the node you want to delete. But this 
# solution requires pointer to the head node which contradicts the problem statement.

# Fast solution is to copy the data from the next node to the node to be deleted and delete the next node. 
# Something like following.






# ############# Not Working




class node(object):
	def __init__(self,x):
		self.data = x
		self.next = None


def deleteNode(node):
	if node.next is None:
		del(node)
	else:
		delNodeUtil(node)
def delNodeUtil(node):
	while(node is not None):
		node.data = node.next.data
		node.next = node.next.next
		free(node.next)
def printList(node):
	while(node is not None):
		print(node.data,'->',end='')
		node=node.next

head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)
printList(head)
deleteNode(head.next.next.next.next)
print()
printList(head)
print()