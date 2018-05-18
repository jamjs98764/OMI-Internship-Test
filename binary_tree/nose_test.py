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

def testBalancedCreate():
	pass
