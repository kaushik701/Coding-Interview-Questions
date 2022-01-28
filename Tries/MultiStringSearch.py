# O(b*n*s) time | O(n) space
def MultiStringSearch(bigString,smallStrings):
	return [isInBigString(bigString,smallString) for smallString in smallStrings]

def isInBigString(bigString,smallString):
	for i in range(len(bigString)):
		if i + len(smallString) > len(bigString):
			break
		if isInBigStringHelper(bigString,smallString,i):
			return True
	return False

def isInBigStringHelper(bigString,smallString,startIdx):
	leftBigIdx = startIdx
	rightBigIdx = startIdx + len(smallString) - 1
	leftSmallIdx = 0
	rightSmallIdx = len(smallString) - 1
	while leftBigIdx <= rightBigIdx:
		if (
			bigString[leftBigIdx] != smallString[leftSmallIdx] or bigString[rightBigIdx] != smallString[rightSmallIdx]
			):
			return False
		leftBigIdx += 1
		rightBigIdx -= 1
		leftSmallIdx += 1
		rightSmallIdx -= 1
	return True

# O(ns+bs) time | O(n) space
def MultiStringSearch1(bigString,smallStrings):
	trie = Trie()
	for string in smallStrings:
		trie.insert(string)
	containedStrings = {}
	for i in range(len(bigString)):
		findSmallStringsIn(bigString,i,trie,containedStrings)
	return [string in containedStrings for string in smallStrings]

def findSmallStringsIn(string,startIdx,trie,containedStrings):
	currentNode = trie.root
	for i in range(startIdx,len(string)):
		currentChar = string[i]
		if currentChar not in currentNode:
			break
		currentNode = currentNode[currentChar]
		if trie.endSymbol in currentNode:
			containedStrings[currentNode[trie.endSymbol]] = True

class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = '*'

	def insert(self,string):
		current = self.root
		for i in range(len(string)):
			if string[i] not in current:
				current[string[i]] = {}
			current = current[string[i]]
		current[self.endSymbol] = string

print(MultiStringSearch('this is a big string',['this','is','not','at','all','a','big','string']))