# O(n) time | O(log(n)) space
def MaxPathSumInBinaryTree(tree):
	_, MaxSum = FindMaxSum(tree)
	return MaxSum

def FindMaxSum(tree):
	if tree is None:
		return (0,0)
	LeftMaxSumAsBranch,LeftMaxPathSum = FindMaxSum(tree.left)
	RightMaxSumAsBranch,RightMaxPathSum = FindMaxSum(tree.right)
	MaxChildSumAsBranch = max(LeftMaxSumAsBranch,RightMaxSumAsBranch)
	value = tree.value
	MaxSumAsBranch = max(MaxChildSumAsBranch+value,value)
	MaxSumAsRootNode = max(LeftMaxSumAsBranch+value+RightMaxSumAsBranch,MaxSumAsBranch)
	MaxPathSum = max(LeftMaxPathSum,RightMaxPathSum,MaxSumAsRootNode)

	return (MaxSumAsBranch,MaxPathSum)	