# Find the middle of a given linked list in C and Java
# Given a singly linked list, find middle of the linked list. For example, if given linked list is 1->2->3->4->5 
# then output should be 3.

# If there are even nodes, then there would be two middle nodes, we need to print second middle element. For example, 
# if given linked list is 1->2->3->4->5->6 then output should be 4.

# One simple method is to travel the whole linked list and count the number of the nodes
# Then travel the linked list till half of the count

class node(object):
	def __init__(self,x):
		self.data = x
		self.next = None

def makeLinkedList(x):
	head = node(x[0])
	temp = head
	for i in range(1,len(x)):
		temp.next = node(x[i])
		temp = temp.next
	return head


# def findMiddle(head):
# 	count = 0
# 	temp = head
# 	while(temp is not None):
# 		count += 1
# 		temp = temp.next
# 	count //= 2
# 	while(count > 0):
# 		head = head.next
# 		count-=1
# 	print(head.data)



# Another approach is to use two pointer 
# one jumps 2 at a time and one jumps 1 at a time
# therfore while the first pointer reaches the end the second pointer will reach the mid

def findMiddle(head):
	temp1 = head
	temp2 = head
	while(temp1 is not None and temp1.next is not None):
		temp1 = temp1.next.next
		temp2 = temp2.next
	print(temp2.data)

head = makeLinkedList([1,2,3,4,5,6,7,8])
findMiddle(head)


