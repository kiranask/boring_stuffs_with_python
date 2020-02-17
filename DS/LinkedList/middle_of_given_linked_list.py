# Python 3 program to find the middle of a
# given linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def append(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	# Function to get the middle of
	# the linked list
	def printMiddle(self):
		slow_ptr = self.head
		fast_ptr = self.head

		if self.head is not None:
			while (fast_ptr is not None and fast_ptr.next is not None):
				fast_ptr = fast_ptr.next.next
				slow_ptr = slow_ptr.next
			print("The middle element is: ", slow_ptr.data)

# Driver code
list1 = LinkedList()
list1.append(5)
list1.append(4)
list1.append(2)
list1.append(3)
list1.append(1)
list1.printMiddle()
