# O(n) time | O(h) space
def CountGoodNodes(root):
	return DFS(root,root.value)

def DFS(node,maxVal):
	if node is None:
		return None
	res = 1 if node.value >= maxVal else 0
	maxVal = max(maxVal,node.value)
	res += DFS(node.left,maxVal)
	res += DFS(node.right,maxVal)
	return res

