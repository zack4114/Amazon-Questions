class node(object):
	def __init__(self,x):
		self.data = x
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.currNode = None
	def push(self,x):
		temp = node(x)
		if self.head is None:
			self.head = temp
		else:
			self.currNode.next = temp
		self.currNode = temp
	def printList(self):
		temp = self.head
		while(temp is not None):
			print(temp.data,'->',end='')
			temp = temp.next
		print()

def segragateListEvenOdd(l):
	temp = l.head
	count = 0
	temphead = None
	prev = None
	while(temp is not None):
		temp = temp.next
		count+=1
	temp = l.head
	while(count > 0):
		if temp.data % 2 == 1:
			l.push(temp.data)
			if prev is not None:
				prev.next = temp.next
		else:
			if temphead is None:
				temphead = temp
				prev = temphead
			else:
				prev = temp
		temp = temp.next
		count-=1
	# l.head = temphead
	return l






# 8->17->15->8->12->10->5->4->1->7->6
l = LinkedList()
l.push(8)
l.push(17)
l.push(15)
l.push(9)
l.push(12)
l.push(10)
l.push(5)
l.push(4)
l.push(1)
l.push(7)
l.push(6)
l.push(69)
l.push(67)
l.printList()
segragateListEvenOdd(l).printList()
