# O(n) time | O(h) space h-height of binary tree
def NodeDepths(root):
	sumOfDepths = 0
	stack = [{"node":root,"depth":0}]
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node,depth = nodeInfo["node"],nodeInfo["depth"]
		if node is None:
			continue
		sumOfDepths += depth
		stack.append({"node":node.left,"depth":depth+1})
		stack.append({"node":node.right,"depth":depth+1})
	return sumOfDepths


# O(n) time | O(h) space h-height of binary tree
def NodeDepths1(root,depth=0):
	if root is None:
		return None
	return depth + NodeDepths1(root.left,depth+1) + NodeDepths1(root.right,depth+1)