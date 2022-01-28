# O(n) time | O(n) space

# InOrder Traverse(left)
# array.append(current.val)
# InOrder Traverse(right)

# array.append(current.val) 
# PreOrder(left)
# PreOrder(right)

# PostOrder(left)
# Postorder(right)
# array.append(current.val)

def InOrderTraverse(tree,array):
	if tree is not None:
		InOrderTraverse(tree.left,array)
		array.append(tree.value)
		InOrderTraverse(tree.right,array)
	return array

def PreOrderTraverse(tree,array):
	if tree is not None:
		array.append(tree.value)
		PreOrderTraverse(tree.left,array)
		PreOrderTraverse(tree.right,array)
	return array

def PostOrderTraverse(tree,array):
	if tree is not None:
		PostOrderTraverse(tree.left,array)
		PostOrderTraverse(tree.right,array)
		array.append(tree.value)
	return array