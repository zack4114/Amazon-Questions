class node(object):
	def __init__(self,x):
		self.data  = x
		self.next =None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.currNode = None
	def push(self,x):
		temp = node(x)
		if self.head == None:
			self.head = temp
		else:
			self.currNode.next = temp
		self.currNode = temp

	def reverseLinkedList(self):
		current = self.head
		prev = None
		next = None
		while(current is not None):
			next = current.next
			current.next= prev
			prev = current
			current = next
		self.head = prev



	def printLinkedList(self):
		temp = self.head
		while(temp is not None):
			print(temp.data,'->',end="")
			temp = temp.next
		print()

l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
l.printLinkedList()
l.reverseLinkedList()
l.printLinkedList()