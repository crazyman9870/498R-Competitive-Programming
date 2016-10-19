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

	#Test that items can be added and removed from a node
	def testNodeAddRemove(self):
		n = Node(4)
		self.assertEqual(n.size(), 0)
		n.add(1)
		self.assertEqual(n.size(), 1)
		n.remove()
		self.assertEqual(n.size(), 0)

	#Tests that if the node capacity has been reached that the program fails appropriately
	@unittest.expectedFailure
	def testNodeAddTooMany(self):
		n = Node(4)
		for i in range(5):
			n.append(i+1)

	#Tests removing an item from the node at a given index
	def testNodeRemoveIndex(self):
		n = Node(4)
		n.add(1)
		self.assertEqual(n.size(), 1)
		n.removeIndex(0)
		self.assertEqual(n.size(), 0)
	
	#Tests attempting to remove from an empty node
	@unittest.expectedFailure
	def testNodeRemoveEmpty(self):
		n = Node(4)
		n.remove()
	
	#Tests attempting to remove from an empty node by index
	@unittest.expectedFailure
	def testNodeRemoveIndexEmpty(self):
		n = Node(4)
		n.removeIndex(2)

	#Tests attempting to remove from a node with an index out of range
	@unittest.expectedFailure
	def testNodeRemoveIndexRangeError(self):
		n = Node(4)
		n.add(1)
		n.add(2)
		self.assertEqual(n.size(), 2)
		n.removeIndex(5)
		self.assertEqual(n.size(), 2)

	#Tests the is full functionaility to indicate if the node is full
	def testNodeIsFull(self):
		n = Node(4)
		n.add(1)
		n.add(2)
		self.assertTrue(not n.isFull())
		n.add(3)
		n.add(4)
		self.assertTrue(n.isFull())

	#Tests that splitting the node is done correctly
	#There should be two lists of equal size and the rounding is done with math.ciel()
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

	#Testing adding a list of itmes into the node
	def testNodeList(self):
		li = [1,2,3,4]
		n = Node(4)
		n.addList(li)
		self.assertEqual(n.size(), 4)

	#Testing adding a list of itmes into that exceeds the max node capacity
	@unittest.expectedFailure
	def testNodeList(self):
		li = [1,2,3,4,5]
		n = Node(4)
		n.addList(li)

	#Test the __str__ function on the node and that it displays correctly
	def testNodeStr(self):
		li = [1,2,3]
		n = Node(4)
		n.addList(li)
		self.assertEqual(str(n), str(li))

	#Tests a custom remove function that removes the first x number of items in the node
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

	#This test is designed to test that the ull is expanding correctly when nodes are
	#filled to capacity and need to divide
	def testNodeExpansion(self):
		ull = UnrolledLinkedList()
		#Fill first node
		for i in range(16):
			ull.append(i+1)
		self.assertEqual(str(ull), '{[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}')
		self.assertEqual(len(ull), 16)
		self.assertEqual(ull.nodeCount, 1)
		#Create first division and fill second node
		for i in range(16,24):
			ull.append(i+1)
		self.assertEqual(str(ull), '{[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]}')
		self.assertEqual(len(ull), 24)
		self.assertEqual(ull.nodeCount, 2)
		#Add one more item to split the node and create 3
		ull.append(25)
		self.assertEqual(str(ull), '{[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24, 25]}')
		self.assertEqual(len(ull), 25)
		self.assertEqual(ull.nodeCount, 3)
	
	#This function is designed to test the getNodeIndexByIndex function
	#This ensures that the value being returned is a tuple conatining a pointer to the node and
	#index in which the data can be found withtin that node
	def testGetNodeFunction(self):
		#Test one item
		ull = UnrolledLinkedList()
		ull.append(1)
		tup = ull.getNodeIndexByIndex(0)
		self.assertEqual(tup[1], 0)
		#Test multiple items
		ull = UnrolledLinkedList()
		#Fill first node
		for i in range(16):
			ull.append(i+1)
		tup = ull.getNodeIndexByIndex(0)
		self.assertEqual(tup[1], 0)
		tup = ull.getNodeIndexByIndex(8)
		self.assertEqual(tup[1], 8)
		tup = ull.getNodeIndexByIndex(15)
		self.assertEqual(tup[1], 15)
		#Test between multiple nodes
		for i in range(16,25):
			ull.append(i+1)
		tup = ull.getNodeIndexByIndex(7)
		self.assertEqual(tup[1], 7)
		tup = ull.getNodeIndexByIndex(8)
		self.assertEqual(tup[1], 0)
		tup = ull.getNodeIndexByIndex(15)
		self.assertEqual(tup[1], 7)
		tup = ull.getNodeIndexByIndex(16)
		self.assertEqual(tup[1], 0)
		tup = ull.getNodeIndexByIndex(20)
		self.assertEqual(tup[1], 4)

	#This test is the same as the one above but test negative indicies which are passed in
	def testGetNodeFunctionNegatives(self):
		#Test one item
		ull = UnrolledLinkedList()
		ull.append(1)
		tup = ull.getNodeIndexByIndex(-1)
		self.assertEqual(tup[1], 0)
		#Test multiple items
		ull = UnrolledLinkedList()
		#Fill first node
		for i in range(16):
			ull.append(i+1)
		tup = ull.getNodeIndexByIndex(-1)
		self.assertEqual(tup[1], 15)
		tup = ull.getNodeIndexByIndex(-8)
		self.assertEqual(tup[1], 8)
		tup = ull.getNodeIndexByIndex(-16)
		self.assertEqual(tup[1], 0)
		#Test between multiple nodes
		for i in range(16,25):
			ull.append(i+1)
		tup = ull.getNodeIndexByIndex(-1)
		self.assertEqual(tup[1], 8)
		tup = ull.getNodeIndexByIndex(-8)
		self.assertEqual(tup[1], 1)
		tup = ull.getNodeIndexByIndex(-9)
		self.assertEqual(tup[1], 0)
		tup = ull.getNodeIndexByIndex(-10)
		self.assertEqual(tup[1], 7)
		tup = ull.getNodeIndexByIndex(-17)
		self.assertEqual(tup[1], 0)
		tup = ull.getNodeIndexByIndex(-25)
		self.assertEqual(tup[1], 0)

	#Test the getNodeIndexByIndex function on empty list expecting failure
	@unittest.expectedFailure
	def testGetNodeFunctionFailEmpty(self):
		ull = UnrolledLinkedList()
		tup = ull.getNodeIndexByIndex(0)

	#Test the getNodeIndexByIndex function with index out of bounds expecting failure
	@unittest.expectedFailure
	def testGetNodeFunctionFail(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		tup = ull.getNodeIndexByIndex(1)

	#Test the getNodeIndexByIndex function with negative index out of bounds expecting failure
	@unittest.expectedFailure
	def testGetNodeFunctionFailNegative(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		tup = ull.getNodeIndexByIndex(-2)
	
	#Test the __getitem__ functionality with positive integers
	def testGetItem(self):
		ull = UnrolledLinkedList()
		for i in range(25):
			ull.append(i+1)
		item = ull[0]
		self.assertEqual(item, 1)
		item = ull[10]
		self.assertEqual(item, 11)
		item = ull[15]
		self.assertEqual(item, 16)
		item = ull[5]
		self.assertEqual(item, 6)
		item = ull[21]
		self.assertEqual(item, 22)
		item = ull[24]
		self.assertEqual(item, 25)

	#Test the __getitem__ functionality with negative integers
	def testGetItemNegative(self):
		ull = UnrolledLinkedList()
		for i in range(25):
			ull.append(i+1)
		item = ull[-1]
		self.assertEqual(item, 25)
		item = ull[-25]
		self.assertEqual(item, 1)
		item = ull[-8]
		self.assertEqual(item, 18)
		item = ull[-16]
		self.assertEqual(item, 10)

	#Test the __getitem__ functionality on empty list
	@unittest.expectedFailure
	def testGetItemFailEmpty(self):
		ull = UnrolledLinkedList()
		item = ull[0]

	#Test the __getitem__ functionality with index out of bounds
	@unittest.expectedFailure
	def testGetItemFail(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		item = ull[1]

	#Test the __getitem__ functionality with negative index out of bounds
	@unittest.expectedFailure
	def testGetItemFailNegative(self):
		ull = UnrolledLinkedList()
		ull.append(1)
		item = ull[-2]

	#Test the __setitem__ functionality replacing values with all sorts of information
	def testSetItem(self):
		ull = UnrolledLinkedList()
		for i in range(20):
			ull.append(i+1)
		#Test first index in first node
		ull[0] = 100
		#Test first index in second node
		ull[8] = 333
		#Test negative numbers
		ull[-1] = 'A'
		ull[-13] = -15.5
		self.assertEqual(str(ull), '{[100, 2, 3, 4, 5, 6, 7, -15.5], [333, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, \'A\']}')

	#Testing the contains function on the list
	def testContains(self):
		ull = UnrolledLinkedList()
		for i in range(20):
			ull.append(i+1)
		self.assertTrue(3 in ull)
		self.assertTrue(7 in ull)
		self.assertFalse(0 in ull)
		self.assertTrue(16 in ull)
		self.assertFalse(21 in ull)

	#Testing the custom private function inRange
	def testInRange(self):
		ull = UnrolledLinkedList()
		self.assertTrue(ull.inRange(1,3,2))
		self.assertTrue(ull.inRange(1,3,1))
		self.assertTrue(ull.inRange(1,3,3))
		self.assertFalse(ull.inRange(1,3,0))
		self.assertFalse(ull.inRange(1,3,-1))
		self.assertFalse(ull.inRange(1,3,5))

	#Testing the reversed iter functionality 
	def testReversed(self):
		ull = UnrolledLinkedList()
		for i in range(25):
			ull.append(i+1)
		testing = []
		for x in reversed(ull):
			testing.append(x)
		self.assertEqual(str(testing), '[25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]')

	#Testing the iter functionality
	def testIter(self):
		ull = UnrolledLinkedList()
		for i in range(25):
			ull.append(i+1)
		testing = []
		for x in ull:
			testing.append(x)
		self.assertEqual(str(testing), '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]')

	#Testing __delitem__ on empty list
	@unittest.expectedFailure
	def testDelItemEmpty(self):
		ull = UnrolledLinkedList()
		del ull[0]
	
	#Testing __delitem__ with index out of bounds
	@unittest.expectedFailure
	def testDelItemIndexError(self):
		ull = UnrolledLinkedList()
		for i in range(6):
			ull.append(i+1)
		del ull[5]
		del ull[5]
		del ull[5]

	#Testing __delitem__ with random indicies
	def testDelItemListSize(self):
		ull = UnrolledLinkedList()
		for i in range(20):
			ull.append(i+1)
		self.assertEqual(len(ull), 20)
		del ull[9]
		self.assertEqual(len(ull), 19)
		del ull[16]
		self.assertEqual(len(ull), 18)
		del ull[2]
		self.assertEqual(len(ull), 17)

	#Testing __delitem__ with random negative indicies
	def testDelItemListSizeNegative(self):
		ull = UnrolledLinkedList()
		for i in range(20):
			ull.append(i+1)
		self.assertEqual(len(ull), 20)
		del ull[-9]
		self.assertEqual(len(ull), 19)
		del ull[-16]
		self.assertEqual(len(ull), 18)
		del ull[-5]
		self.assertEqual(len(ull), 17)

	#Testing rebalancing after __delitem__  that would cause multiple different cases
	#Primarily done with two largish nodes
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

		#Test 2 nodes
		ull = UnrolledLinkedList()
		for i in range(17):
			ull.append(i+1)
		self.assertEqual(str(ull), '{[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17]}')
		del ull[0]
		self.assertEqual(str(ull), '{[2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17]}')
		del ull[0]
		del ull[0]
		self.assertEqual(str(ull), '{[4, 5, 6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17]}')
		del ull[7]
		del ull[7]
		self.assertEqual(str(ull), '{[4, 5, 6, 7, 8, 9, 10, 13, 14], [15, 16, 17]}')
		del ull[7]
		del ull[7]
		self.assertEqual(str(ull), '{[4, 5, 6, 7, 8, 9, 10, 15, 16], [17]}')
		del ull[7]
		del ull[7]
		self.assertEqual(str(ull), '{[4, 5, 6, 7, 8, 9, 10, 17]}')
	
	#Testing rebalancing after __delitem__  that would cause multiple different cases
	#Focus on creating a list that the deletion would cause a chain reaction to the rebalancing
	#multiple nodes
	def testDelItemWithRebalanceLarge(self):
		#Test 3 nodes
		ull = UnrolledLinkedList()
		for i in range(25):
			ull.append(i+1)
		self.assertEqual(str(ull), '{[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23, 24, 25]}')

		'''
		First delete one off the first node which should cause a chain reaction
		Start 8->8->9
		Del one off first node
		7->8->9
		Should change to
		9->6->9
		Should change to
		9->9->6
		'''
		del ull[0]
		self.assertEqual(str(ull), '{[2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25]}')
		
