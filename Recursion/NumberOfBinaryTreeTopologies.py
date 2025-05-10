# O(n*(2n)!/(n!(n+1)!))) time | O(n) space
def getNumberOfBinaryTreeTopologies(n):
	if n == 0:
		return 1
	numberOfTrees = 0
	for leftTreeSize in range(n):
		rightTreeSize = n - 1 - leftTreeSize
		numberOfLeftTrees = getNumberOfBinaryTreeTopologies(leftTreeSize)
		numberOfRightTrees = getNumberOfBinaryTreeTopologies(rightTreeSize)
		numberOfTrees += numberOfLeftTrees * numberOfRightTrees
	return numberOfTrees

# O(n^2) time | O(n) space
def getNumberOfBinaryTreeTopologies2(n,cache={0:1}):
	if n is cache:
		return cache[n]
	numberOfTrees = 0
	for leftTreeSize in range(n):
		rightTreeSize = n - 1 - leftTreeSize
		numberOfLeftTrees = getNumberOfBinaryTreeTopologies2(leftTreeSize,cache)
		numberOfRightTrees = getNumberOfBinaryTreeTopologies2(rightTreeSize,cache)
		numberOfTrees += numberOfLeftTrees * numberOfRightTrees
	cache[n] = numberOfTrees
	return numberOfTrees

# O(n^2) time | O(n) space
def getNumberOfBinaryTreeTopologies3(n):
	cache = [1]
	for m in range(1,n+1):
		numberOfTrees = 0
		for leftTreeSize in range(m):
			rightTreeSize = m - 1 - leftTreeSize
			numberOfLeftTrees = cache[leftTreeSize]
			numberOfRightTrees = cache[rightTreeSize]
			numberOfTrees += numberOfLeftTrees * numberOfRightTrees
		cache.append(numberOfTrees)
	return cache[n]

print(getNumberOfBinaryTreeTopologies(6))
print(getNumberOfBinaryTreeTopologies3(6))