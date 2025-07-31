class BinarySearchTree:
	def __init__(self,value=0,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right

# O(h) time | O(h) space
def ValidateThreeNodes(nodeOne, nodeTwo, nodeThree):
	if isDescendant(nodeTwo, nodeOne):
		return isDescendant(nodeThree, nodeTwo)

	if isDescendant(nodeTwo, nodeThree):
		return isDescendant(nodeOne, nodeTwo)

	return False

def isDescendant(node, target):
	if node is None:
		return False

	if node is target:
		return True

	return isDescendant(node.left, target) if target.value < node.value else isDescendant(node.right, target)


# O(h) time | O(1) space
def ValidateThreeNodes1(nodeOne, nodeTwo, nodeThree):
	if isDescendant1(nodeTwo, nodeOne):
		return isDescendant1(nodeThree, nodeTwo)

	if isDescendant(nodeTwo, nodeThree):
		return isDescendant1(nodeOne, nodeTwo)

	return False

def isDescendant1(node, target):
	while node is not None and node is not target:
		node = node.left if node.value > target.value else node.right
	return node is target

# O(d) time | O(1) space
def ValidateThreeNodes2(nodeOne, nodeTwo, nodeThree):
	searchOne = nodeOne
	searchTwo = nodeTwo

	while True:
		foundThreeFromOne = searchOne is nodeThree
		foundOneFromThree = searchTwo is nodeOne
		foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
		finishedSearching = searchOne is None and searchTwo is None
		if foundThreeFromOne or foundOneFromThree or foundNodeTwo or finishedSearching:
			break

		if searchOne is not None:
			searchOne = searchOne.left if searchOne.value > nodeTwo.value else searchOne.right

		if searchTwo is not None:
			searchTwo = searchTwo.left if searchTwo.value > nodeTwo.value else searchTwo.right

	foundNodeFromOther = searchOne is nodeThree or searchTwo is nodeOne
	foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
	if not foundNodeTwo or foundNodeFromOther:
		return False

	return searchForTarget(nodeTwo, nodeThree if searchOne is nodeTwo else nodeOne)

def searchForTarget(node, target):
	while node is not None and node is not target:
		node = node.left if node.value > target.value else node.right
	return node is target