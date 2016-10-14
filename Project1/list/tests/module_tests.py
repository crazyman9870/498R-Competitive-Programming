''' You will need the following import if using python2 '''
# from __future__ import absolute_import

from ..unrolled_linked_list.module import UnrolledLinkedList
from ..unrolled_linked_list.LLNode import Node
import unittest


class UnrolledLinkedList_Test(unittest.TestCase):
	"""This is an example of a Testing class. You are welcome to make multiple
	classes to organize your code if you would like to, but it is in no way
	required or expected. You'll want to replace this comment with your own.
	"""
	def test_default_node_capacity(self):
		"""Test that the default node capacity is being set, and is set to 16
		"""
		l = UnrolledLinkedList()
		self.assertEqual(l.max_node_capacity, 16)
	
	#Node class unit tests

	def testNodeAddRemove(self):
		n = Node(4)
		self.assertEqual(n.size(), 0)
		n.add(1)
		self.assertEqual(n.size(), 1)
		n.remove()
		self.assertEqual(n.size(), 0)

	@unittest.expectedFailure
	def testNodeAddTooMany(self):
		n = Node(4)
		for i in range(5):
			n.append(i+1)

	def testNodeRemoveIndex(self):
		n = Node(4)
		n.add(1)
		self.assertEqual(n.size(), 1)
		n.removeIndex(0)
		self.assertEqual(n.size(), 0)
	
	@unittest.expectedFailure
	def testNodeRemoveEmpty(self):
		n = Node(4)
		n.remove()
	
	@unittest.expectedFailure
	def testNodeRemoveIndexEmpty(self):
		n = Node(4)
		n.removeIndex(2)

	@unittest.expectedFailure
	def testNodeRemoveIndexRangeError(self):
		n = Node(4)
		n.add(1)
		n.add(2)
		self.assertEqual(n.size(), 2)
		n.removeIndex(5)
		self.assertEqual(n.size(), 2)

	def testNodeIsFull(self):
		n = Node(4)
		n.add(1)
		n.add(2)
		self.assertTrue(not n.isFull())
		n.add(3)
		n.add(4)
		self.assertTrue(n.isFull())

	def testNodeSplit(self):
		n = Node(4)
		n.add(1)
		n.add(2)
		n.splitNode()
		self.assertEqual(n.size(), 2)
		n.add(3)
		n.add(4)
		self.assertEqual(n.size(), 4)
		l = n.splitNode()
		self.assertEqual(n.size(), 2)
		self.assertEqual(len(l), 2)

	def testNodeList(self):
		li = [1,2,3,4]
		n = Node(4)
		n.addList(li)
		self.assertEqual(n.size(), 4)

	@unittest.expectedFailure
	def testNodeList(self):
		li = [1,2,3,4,5]
		n = Node(4)
		n.addList(li)

	def testNodeStr(self):
		li = [1,2,3]
		n = Node(4)
		n.addList(li)
		self.assertEqual(str(n), str(li))

	def testNodeRemoveFirstXItems(self):
		li = [1,2,3,4]
		n = Node(4)
		n.addList(li)
		newList = n.removeFirstXItems(2)
		self.assertEqual(len(newList), 2)
		newList = n.removeFirstXItems(1)
		self.assertEqual(len(newList), 1)
		newList = n.removeFirstXItems(2)
		self.assertEqual(len(newList), 1)

	#Unrolled Linked List unit tests

	def testNodeExpansion(self):
		ull = UnrolledLinkedList()
		for i in range(16):
			ull.append(i+1)
		self.assertEqual(len(ull), 16)
		self.assertEqual(ull.nodeCount, 1)
		print(ull)
		ull.append(3)
		ull.append(4)
		print(ull)
	'''
	def testGetNodeFunction(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		tup = ull.getNodeIndexByIndex(0)
		self.assertEqual(tup[1], 0)
		ull.append(2)
		tup = ull.getNodeIndexByIndex(1)
		self.assertEqual(tup[1], 1)
		ull.append(3)
		ull.append(4)
		tup = ull.getNodeIndexByIndex(3)
		self.assertEqual(tup[1], 3)
		ull.append(5)
		ull.append(6)
		tup = ull.getNodeIndexByIndex(1)
		self.assertEqual(tup[1], 1)
		tup = ull.getNodeIndexByIndex(3)
		self.assertEqual(tup[1], 1)
		tup = ull.getNodeIndexByIndex(5)
		self.assertEqual(tup[1], 3)
		ull.append(7)
		tup = ull.getNodeIndexByIndex(3)
		self.assertEqual(tup[1], 1)
		tup = ull.getNodeIndexByIndex(5)
		self.assertEqual(tup[1], 1)

	def testGetNodeFunctionNegatives(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		tup = ull.getNodeIndexByIndex(-1)
		self.assertEqual(tup[1], 0)
		ull.append(2)
		tup = ull.getNodeIndexByIndex(-2)
		self.assertEqual(tup[1], 0)
		ull.append(3)
		ull.append(4)
		tup = ull.getNodeIndexByIndex(-2)
		self.assertEqual(tup[1], 2)
		ull.append(5)
		ull.append(6)
		tup = ull.getNodeIndexByIndex(-6)
		self.assertEqual(tup[1], 0)
		tup = ull.getNodeIndexByIndex(-4)
		self.assertEqual(tup[1], 0)
		tup = ull.getNodeIndexByIndex(-1)
		self.assertEqual(tup[1], 3)
		ull.append(7)
		tup = ull.getNodeIndexByIndex(-4)
		self.assertEqual(tup[1], 1)
		tup = ull.getNodeIndexByIndex(-2)
		self.assertEqual(tup[1], 1)

	@unittest.expectedFailure
	def testGetNodeFunctionFailEmpty(self):
		ull = UnrolledLinkedList()
		tup = ull.getNodeIndexByIndex(0)

	@unittest.expectedFailure
	def testGetNodeFunctionFail(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		tup = ull.getNodeIndexByIndex(1)

	@unittest.expectedFailure
	def testGetNodeFunctionFailNegative(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		tup = ull.getNodeIndexByIndex(-2)

	def testGetItem(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		item = ull[0]
		self.assertEqual(item, 1)
		ull.append(2)
		item = ull[1]
		self.assertEqual(item, 2)
		ull.append(3)
		ull.append(4)
		item = ull[3]
		self.assertEqual(item, 4)
		ull.append(5)
		ull.append(6)
		item = ull[1]
		self.assertEqual(item, 2)
		item = ull[3]
		self.assertEqual(item, 4)
		item = ull[5]
		self.assertEqual(item, 6)
		ull.append(7)
		item = ull[3]
		self.assertEqual(item, 4)
		item = ull[5]
		self.assertEqual(item, 6)

	def testGetItemNegative(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		item = ull[-1]
		self.assertEqual(item, 1)
		ull.append(2)
		item = ull[-1]
		self.assertEqual(item, 2)
		ull.append(3)
		ull.append(4)
		item = ull[-1]
		self.assertEqual(item, 4)
		ull.append(5)
		ull.append(6)
		item = ull[-5]
		self.assertEqual(item, 2)
		item = ull[-3]
		self.assertEqual(item, 4)
		item = ull[-1]
		self.assertEqual(item, 6)
		ull.append(7)
		item = ull[-4]
		self.assertEqual(item, 4)
		item = ull[-2]
		self.assertEqual(item, 6)

	@unittest.expectedFailure
	def testGetItemFailEmpty(self):
		ull = UnrolledLinkedList()
		item = ull[0]

	@unittest.expectedFailure
	def testGetItemFail(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		item = ull[1]

	@unittest.expectedFailure
	def testGetItemFailNegative(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		item = ull[-2]

	def testSetItem(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		ull.append(5)
		ull.append(6)
		ull.append(7)
		ull.append(8)
		self.assertEqual(str(ull), '{[1, 2],[3, 4],[5, 6, 7, 8]}')
		ull[6] = 100
		ull[2] = 333
		ull[-8] = -15
		ull[-4] = 'A'
		self.assertEqual(str(ull), '{[-15, 2],[333, 4],[\'A\', 6, 100, 8]}')

	def testContains(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		ull.append(5)
		ull.append(6)
		ull.append(7)
		ull.append(8)
		self.assertEqual(str(ull), '{[1, 2],[3, 4],[5, 6, 7, 8]}')
		self.assertTrue(3 in ull)
		self.assertTrue(7 in ull)
		self.assertFalse(0 in ull)

	def testInRange(self):
		ull = UnrolledLinkedList()
		self.assertTrue(ull.inRange(1,3,2))
		self.assertTrue(ull.inRange(1,3,1))
		self.assertTrue(ull.inRange(1,3,3))
		self.assertFalse(ull.inRange(1,3,0))
		self.assertFalse(ull.inRange(1,3,-1))
		self.assertFalse(ull.inRange(1,3,5))

	def testReversed(self):
		ull = UnrolledLinkedList()
		reversed(ull)
		self.assertEqual(str(ull), '{}')
		ull.append(1)
		reversed(ull)
		self.assertEqual(str(ull), '{[1]}')
		ull.append(2)
		self.assertEqual(str(ull), '{[1, 2]}')
		reversed(ull)
		self.assertEqual(str(ull), '{[2, 1]}')
		reversed(ull)
		self.assertEqual(str(ull), '{[1, 2]}')
		ull.append(3)
		ull.append(4)
		self.assertEqual(str(ull), '{[1, 2, 3, 4]}')
		reversed(ull)
		self.assertEqual(str(ull), '{[4, 3, 2, 1]}')
		reversed(ull)
		self.assertEqual(str(ull), '{[1, 2, 3, 4]}')
		ull.append(5)
		ull.append(6)
		ull.append(7)
		self.assertEqual(str(ull), '{[1, 2],[3, 4],[5, 6, 7]}')
		reversed(ull)
		self.assertEqual(str(ull), '{[7, 6],[5, 4],[3, 2, 1]}')
		reversed(ull)
		self.assertEqual(str(ull), '{[1, 2],[3, 4],[5, 6, 7]}')

	def testIter(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		ull.append(5)
		ull.append(6)
		ull.append(7)
		self.assertEqual(str(ull), '{[1, 2],[3, 4],[5, 6, 7]}')
		testing = []
		for x in ull:
			testing.append(x)
		self.assertEqual(str(testing), '[1, 2, 3, 4, 5, 6, 7]')
		testing = []
		reversed(ull)
		for x in ull:
			testing.append(x)
		self.assertEqual(str(testing), '[7, 6, 5, 4, 3, 2, 1]')

	@unittest.expectedFailure
	def testDelItemEmpty(self):
		ull = UnrolledLinkedList()
		del ull[0]
	
	@unittest.expectedFailure
	def testDelItemIndexError(self):
		ull = UnrolledLinkedList()
		ull.append(0)
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		ull.append(5)
		ull.append(6)
		del ull[5]
		del ull[5]
		del ull[5]

	def testDelItemListSize(self):
		ull = UnrolledLinkedList()
		ull.append(0)
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		ull.append(5)
		ull.append(6)
		self.assertEqual(len(ull), 7)
		del ull[5]
		self.assertEqual(len(ull), 6)
		del ull[5]
		self.assertEqual(len(ull), 5)
		del ull[2]
		self.assertEqual(len(ull), 4)

	def testDelItemListSizeNegative(self):
		ull = UnrolledLinkedList()
		ull.append(0)
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		ull.append(5)
		ull.append(6)
		self.assertEqual(len(ull), 7)
		del ull[-7]
		self.assertEqual(len(ull), 6)
		del ull[-6]
		self.assertEqual(len(ull), 5)
		del ull[-2]
		self.assertEqual(len(ull), 4)

	def testDelItemWithRebalanceSmall(self):
		ull = UnrolledLinkedList()
		#Test 1 item in list
		ull.append(0)
		del ull[0]
		self.assertEqual(len(ull), 0)
		self.assertEqual(ull.nodeCount, 0)
		self.assertEqual(str(ull), '{}')

		#Test 2 items in list
		ull.append(0)
		ull.append(1)
		del ull[0]
		self.assertEqual(len(ull), 1)
		self.assertEqual(ull.nodeCount, 1)
		self.assertEqual(str(ull), '{[1]}')
		#Clear
		del ull[0]

		#Test [2itmes]->[1item]
		ull.append(0)
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		del ull[3]
		del ull[3]
		self.assertEqual(len(ull), 3)
		del ull[1]
		self.assertEqual(len(ull), 2)
		self.assertEqual(ull.nodeCount, 1)
		self.assertEqual(str(ull), '{[0, 2]}')
		#Clear
		del ull[0]
		del ull[0]

		#Test [2items]->[2items]
		ull.append(0)
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		del ull[4]
		self.assertEqual(len(ull), 4)
		del ull[0]
		self.assertEqual(len(ull), 3)
		self.assertEqual(ull.nodeCount, 1)
		self.assertEqual(str(ull), '{[1, 2, 3]}')
		#Clear
		del ull[0]
		del ull[0]
		del ull[0]

		#Test [2items]->[3items]
		ull.append(0)
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		self.assertEqual(len(ull), 5)
		del ull[0]
		self.assertEqual(len(ull), 4)
		self.assertEqual(ull.nodeCount, 2)
		self.assertEqual(str(ull), '{[1, 2, 3],[4]}')
		#Clear
		del ull[0]
		del ull[0]
		del ull[0]
		del ull[0]

		#Test [2items]->[4items]
		ull.append(0)
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		ull.append(5)
		self.assertEqual(len(ull), 6)
		del ull[0]
		self.assertEqual(len(ull), 5)
		self.assertEqual(ull.nodeCount, 2)
		self.assertEqual(str(ull), '{[1, 2, 3],[4, 5]}')
		#Clear
		del ull[0]
		del ull[0]
		del ull[0]
		del ull[0]
		del ull[0]

	def testDelItemWithRebalanceLarge(self):
		ull = UnrolledLinkedList()
		ull.append(0)
		ull.append(1)
		ull.append(2)
		ull.append(3)
		ull.append(4)
		ull.append(5)
		ull.append(6)
		ull.append(7)
		ull.append(8)
		ull.append(9)
		ull.append(10)
		self.assertEqual(len(ull), 11)
		self.assertEqual(ull.nodeCount, 5)

		#Pull one out of the middle to get combined two in the middle
		del ull[3]
		self.assertEqual(len(ull), 10)
		self.assertEqual(ull.nodeCount, 4)
		self.assertEqual(str(ull), '{[0, 1],[2, 4, 5],[6, 7],[8, 9, 10]}')

		#Now delete 0 to create mutliple cases
		#First node should grab 2 and 4 leaving the second node with just 5
		#Second node should then grab 6 and 7
		#Third node should then be deleted from the list
		#Should result in 3 nodes with 3 items in each one
		del ull[0]
		self.assertEqual(len(ull), 9)
		self.assertEqual(ull.nodeCount, 3)
		self.assertEqual(str(ull), '{[1, 2, 4],[5, 6, 7],[8, 9, 10]}')

		#Delete 2 and 4 and create more imbalances
		del ull[1]
		del ull[1]
		self.assertEqual(len(ull), 7)
		self.assertEqual(ull.nodeCount, 3)
		self.assertEqual(str(ull), '{[1, 5, 6],[7, 8, 9],[10]}')

		#Insert more data of all types
		ull.append([])
		ull.append('a')
		ull.append('b')
		ull.append(-5)
		ull.append(100)
		self.assertEqual(str(ull), '{[1, 5, 6],[7, 8, 9],[10, []],[\'a\', \'b\', -5, 100]}')

		#Final test
		#List looks like
		#[3items]->[3items]->[2item]->[4items]

		#By causing the first node to go under half full
		#we should see that it should cause an imbalance in the second node
		#that should then pull from a third node causing it to go empty and be removed

		del ull[1]
		del ull[1]
		self.assertEqual(len(ull), 10)
		self.assertEqual(ull.nodeCount, 3)
		self.assertEqual(str(ull), '{[1, 7, 8],[9, 10, []],[\'a\', \'b\', -5, 100]}')
		'''