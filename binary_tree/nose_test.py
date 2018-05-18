import os, shutil
import sys
from tree import *

######
# Part 1: Test Insertion and Search functions
#####

# Normal case
def testInsertionSearch1():
	myTree = binaryTree(11)
	testList = [10,4,5,45,21,54,3]
	# Solution:		
	#		11
	#	10		45
	# 4		  21  54
	#3 5
	target = 4
	for item in testList:
		myTree.insertNode(item)
	assert checkTreeFixed(myTree,target) == (3,[11,10])

# Boundary case - target is at root
def testInsertionSearch2():
	myTree = binaryTree(11)
	testList = [10,4,5,45,21,54,3]
	# Solution:		
	#		11
	#	10		45
	# 4		  21  54
	#3 5
	target = 11
	for item in testList:
		myTree.insertNode(item)
	assert checkTreeFixed(myTree,target) == (1,[])

# Boundary case - target is not there
def testInsertionSearch3():
	myTree = binaryTree(11)
	testList = [10,4,5,45,21,54,3]
	# Solution:		
	#		11
	#	10		45
	# 4		  21  54
	#3 5
	target = 12
	for item in testList:
		myTree.insertNode(item)
	assert checkTreeFixed(myTree,target) == (0,[]) 

######
# Part 2: Test BST balance
#####


# Normal case:
def testBalancedTrue():
	myTree = binaryTree(11)
	testList = [13,2,1,3,12,14]
	# Solution:
	#		11
	#	2		13
	# 1   3   12  14
	for item in testList:
		myTree.insertNode(item)
	assert checkBalance(myTree) == True
	assert treeHeight(myTree) == 3

# Bounary case: tree with single node always balanced
def testBalancedTrue1():
	myTree = binaryTree(11)
	testList = []
	# Solution:
	#		11
	for item in testList:
		myTree.insertNode(item)
	assert checkBalance(myTree) == True
	assert treeHeight(myTree) == 1

# Boundary case: Diff min max height = 1
def testBalancedTrue2():
	myTree = binaryTree(11)
	testList = [13,2,1,3]
	# Solution:
	#		11
	#	2		13
	# 1   3  
	for item in testList:
		myTree.insertNode(item)
	assert checkBalance(myTree) == True
	assert treeHeight(myTree) == 3

# Boundary case: Diff min max height = 2
def testBalancedFalse():
	myTree = binaryTree(11)
	testList = [13,2,1,3,4]
	# Solution:
	#		11
	#	2		13
	# 1   3   
	#      4
	for item in testList:
		myTree.insertNode(item)
	assert checkBalance(myTree) == False

######
# Part 3: Creating balanced tree from 
#####

def testBalancedCreate():
	testList = [3,2,1,4,6,5,7,81]
	testTree = createBalancedTree(testList)
	# Solution:
	#		5
	#	 3	   7
	#  2  4   6  8
	#1      	
	assert testTree.left.left.left.getValue() == 1
	assert testTree.right.left.getValue() == 6