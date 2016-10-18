import sys
from ..unrolled_linked_list.LLNode import Node

class UnrolledLinkedList():

	def __init__(self, max_node_capacity=16):
		self.max_node_capacity = max_node_capacity
		self.size = 0
		self.nodeCount = 0
		self.head = None

	def __delitem__(self, index):
		#Grab Node and Index Tuple
		tup = self.getNodeIndexByIndex(index)
		#Remove the item from the list
		tup[0].removeIndex(tup[1])
		self.size -= 1
		#Rebalance the list
		if self.head is not None and self.size == 0:
			del self.head
			self.nodeCount = 0
			self.head = None
		else:
			self.rebalance(tup[0])

	def __getitem__(self,index):
		tup = self.getNodeIndexByIndex(index)
		return tup[0][tup[1]]

	def __setitem__(self,key,value):
		tup = self.getNodeIndexByIndex(key)
		tup[0][tup[1]] = value

	def __iter__(self):
		temp = self.head
		while temp is not None:
			for x in temp:
				yield x
			temp = temp.next

	def __str__ (self):
		if self.head is None:
			return '{}'

		string = []
		temp = self.head
		while temp is not None:
			string.append(str(temp))
			#string.append(str(temp))
			temp = temp.next
		return '{' + ', '.join(str(x) for x in string) + '}'

	def __len__(self):
		return self.size

	def __reversed__(self):
		#Base Cases
		if self.head is None:
			raise TypeError() 
		if self.size == 1:
			return

		temp = self.head
		items = []
		while temp is not None:
			items += temp.data
			temp = temp.next

		temp = self.head
		while temp is not None:
			for i in range(len(temp)):
				temp[i] = items[len(items) - 1]
				items.pop()
			temp = temp.next

	def __contains__(self,obj):
		#Base Case
		if self.head is None:
			return False

		temp = self.head
		while temp is not None:
			if obj in temp:
				return True
			temp = temp.next

		return False

	def append(self,data):
		#Base Case
		if self.head is None:
			self.head = Node(self.max_node_capacity)
			self.head.add(data)
			self.size = 1
			self.nodeCount = 1
			return

		temp = self.head
		while temp.next is not None:
			temp = temp.next

		if temp.isFull():
			newList = temp.splitNode()
			temp.next = Node(self.max_node_capacity)
			temp.next.addList(newList)
			temp.next.add(data)
			self.size += 1
			self.nodeCount += 1
		else:
			temp.add(data)
			self.size += 1

	def rebalance(self, startNode):
		temp = startNode.next
		minSize = startNode.maxSize // 2
		while temp is not None:
			if len(startNode) < minSize:
				itemsNeeded = minSize + 1 - len(startNode)
				newItems = temp.removeFirstXItems(itemsNeeded)
				startNode.addList(newItems)
				if temp.isEmpty():
					n = temp.next
					startNode.next = n
					del temp
					self.nodeCount -= 1
				startNode = startNode.next
				if startNode is None:
					temp = None
				else:
					temp = startNode.next
			else:
				break

	def getNodeIndexByIndex(self, index):
		#Base Cases
		if self.head is None:
			raise Exception('List is empty')
		#Check to see if the abs of the index is in range
		if index < 0:
			index = self.convertNegativeIndex(index)
		if index >= self.size or index < 0:
			raise IndexError()

		#Find the node
		temp = self.head
		iMin = 0
		iMax = len(temp) - 1
		while not self.inRange(iMin, iMax, index):
			temp = temp.next
			iMin = iMax + 1
			iMax += len(temp)

		i = index - iMin
		return (temp, i)

	def nodeCount(self):
		return self.nodeCount

	def inRange(self, low, high, i):
		if i >= low and i <= high:
			return True
		else:
			return False

	def convertNegativeIndex(self, index):
		return self.size + index