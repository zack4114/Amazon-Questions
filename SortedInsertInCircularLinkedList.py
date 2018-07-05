# Sorted insert for circular linked list
# Difficulty Level: Rookie
# Write a C function to insert a new value in a sorted Circular Linked List (CLL). For example, 
# if the input CLL is following.
# 3->7->9->11
# insert(8)
# 3->7->8->9->11

# Not completed



class node(object):
	def __init__(self,x):
		self.data = x
		self.next = None

class CircularLinkedList(object):
	def __init__(self):
		self.head = None
		self.currNode = None

	def sortedInsert(self,x):
		newNode = node(x)

	def printList(self):
		temp = self.head.next
		temp1 = self.head
		while(temp != temp1):
			print(temp.data,'->',end='')
			temp = temp.next
		print(temp.data,'->',end='')
		print()
l = CircularLinkedList()
l.sortedInsert(1)
l.sortedInsert(2)
l.sortedInsert(3)
l.sortedInsert(4)
l.sortedInsert(5)
l.printList()

