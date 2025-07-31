# Leetcode #534: https://youtu.be/bkxqA8Rfv04?si=Ja0n2AW9Ck9AycVJ
# O(n) time | O(h) space
class BinaryTree:
	def __init__(self,value,left,right):
		self.value = value
		self.left = left
		self.right = right

def DiameterOfBinaryTree(root):
	res = [0]
	DepthFirstSearch(root)
	return res[0]

def DepthFirstSearch(root):
	if root is None:
		return -1
	left = DepthFirstSearch(root.left)
	right = DepthFirstSearch(root.right)
	res[0] = max(res[0],(left+right+2))
	return max(left,right) + 1

# O(n) time | O(n) space
def DiameterOfBinaryTree1(tree):
	return getTreeInfo(tree).diameter

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo()
	leftTreeData = getTreeInfo(tree.left)
	rightTreeData = getTreeInfo(tree.right)

	longestPathThroughRoot = leftTreeData.height + rightTreeData.height
	maxDiameterSoFar = max(leftTreeData.diameter, rightTreeData.diameter)
	currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
	currentHeight = 1 + max(leftTreeData.height, rightTreeData.height)

	return TreeInfo(currentDiameter, currentHeight)

class TreeInfo:
	def __init__(self,diameter,height):
		self.diameter = diameter
		self.height = height