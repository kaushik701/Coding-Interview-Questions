# O(n) time | O(1) space
array = list(map(int,input('Enter the Number: ').split()))
def hasSingleCycle(array):
	numElementsvisited = 0
	currentIdx = 0
	while numElementsvisited < len(array):
		if numElementsvisited > 0 and currentIdx == 0:
			return False
		numElementsvisited += 1
		currentIdx = getNextIdx(currentIdx,array)
	return currentIdx == 0

def getNextIdx(currentIdx,array):
	jump = array[currentIdx]
	nextIdx = (currentIdx + jump) % len(array)
	if nextIdx >= 0:
		return nextIdx
	else:
		return nextIdx + len(array)

print(hasSingleCycle(array))