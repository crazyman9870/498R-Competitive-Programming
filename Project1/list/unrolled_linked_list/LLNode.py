import sys

class Node():

		def __init__(self, maxSize):
			self.maxSize = maxSize
			self.data = []
			self.next = None

		def __del__(self):
			self.next = None
			del self.data

		def __str__(self):
			return str(self.data)

		def __len__(self):
			return len(self.data)

		def __getitem__(self, index):
			return self.data[index]

		def __setitem__(self,key,value):
			self.data[key] = value

		def __contains__(self,obj):
			if obj in self.data:
				return True
			else:
				return False

		def __iter__(self):
			for x in self.data:
				yield x

		def add(self, item):
			if self.isFull():
				raise Exception('Node is full')
			self.data.append(item)

		def addList(self, newList):
			if len(newList) > self.maxSize:
				raise Exception('New list is greater than max list size')
			self.data += newList

		def isFull(self):
			if len(self.data) == self.maxSize:
				return True
			else:
				return False

		def isEmpty(self):
			if len(self.data) == 0:
				return True
			else:
				return False

		def size(self):
			return len(self.data)

		def remove(self):
			return self.data.pop()

		def removeFirstItem(self):
			return self.data.pop(0)

		def removeIndex(self, index):
			if index >= 0 and index < self.maxSize:
				return self.data.pop(index)
			else:
				raise IndexError()

		def removeFirstXItems(self, x):
			newList = []
			for i in range(x):
				if not self.isEmpty():
					newList.append(self.removeFirstItem())
			return newList

		def splitNode(self):
			if self.isFull():
				split = []
				newSize = self.size() // 2
				while self.size() > newSize:
					split.append(self.removeIndex(newSize))
				return split