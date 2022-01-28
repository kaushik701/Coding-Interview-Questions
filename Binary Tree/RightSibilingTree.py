# O(n) time | O(d) space
def RightSiblingTree(root):
	mutate(root,None,None)
	return root

def mutate(node,parent,isLeftChild):
	if node is None:
		return
	left,right = node.left,node.right
	mutate(left,node,True)
	if parent is None:
		node.right = None
	elif isLeftChild:
		node.right = parent.right
	else:
		if parent.right is None:
			node.right = None
		else:
			node.right = parent.right.left
	mutate(right,node,False) 