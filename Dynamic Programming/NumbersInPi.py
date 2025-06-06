# O(n^3 + m) time | O (n+m) space
def NumbersInPi(pi,numbers):
	numbersTable = {number:True for number in numbers}
	minSpaces = getMinSpaces(pi,numbersTable,{},0)
	return -1 if minSpaces == float('inf') else minSpaces

def getMinSpaces(pi,numbersTable,cache,idx):
	if idx ==  len(pi):
		return -1
	if idx in cache:
		return cache[idx]
	minSpaces = float("inf")
	for i in range(idx,len(pi)):
		prefix = pi[idx:i+1]
		if prefix in numbersTable:
			minSpacesinSuffix = getMinSpaces(pi, numbersTable, cache,i+1)
			minSpaces = min(minSpaces,minSpacesinSuffix+1)
	cache[idx] = minSpaces
	return cache[idx]


# O(n^3 + m) time | O (n+m) space
def NumbersInPi1(pi,numbers):
	numbersTable = {number:True for number in numbers}
	cache = {}
	for i in reversed(range(len(pi))):
		getMinSpaces1(pi,numbersTable,cache,i)
	return -1 if cache[0] == float('inf') else cache[0]

def getMinSpaces1(pi,numbersTable,cache,idx):
	if idx ==  len(pi):
		return -1
	if idx in cache:
		return cache[idx]
	minSpaces = float("inf")
	for i in range(idx,len(pi)):
		prefix = pi[idx:i+1]
		if prefix in numbersTable:
			minSpacesinSuffix = getMinSpaces(pi, numbersTable, cache,i+1)
			minSpaces = min(minSpaces,minSpacesinSuffix+1)
	cache[idx] = minSpaces
	return cache[idx]