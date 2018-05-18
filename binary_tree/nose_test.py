import os, shutil
import sys
from tree import *


def testInsertionSearch():
	myTree = binaryTree(11)
	testList = [10,4,5,45,21,54,3]
	target = 4
	for item in testList:
		myTree.insertNode(item)
	myTree.printDepthWise()
	assert checkTreeFixed(myTree,target) == (3,[11,10])

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


