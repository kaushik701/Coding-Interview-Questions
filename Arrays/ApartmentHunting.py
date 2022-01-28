# O(b^2 * r) time | O(b) space
def apartmentHunting(blocks,reqs):
	maxDistAtBlocks = [float('-inf') for block in blocks]
	for i in range(len(blocks)):
		for req in reqs:
			clossestReqDistance = float('inf')
			for j in range(len(blocks)):
				if blocks[j][req]:
					clossestReqDistance = min(clossestReqDistance,distanceBetween(i,j))
			maxDistAtBlocks[i] = max(maxDistAtBlocks[i],clossestReqDistance)
	return getIdxAtMinValue(maxDistAtBlocks)

def getIdxAtMinValue(array):
	idxAtMinValue = 0
	minValue = float('inf')
	for i in range(len(array)):
		currentValue = array[i]
		if currentValue < minValue:
			minValue = currentValue
			idxAtMinValue = i
	return idxAtMinValue

def distanceBetween(a,b):
	return abs(a-b)

#----------------------------------------------------------------



# O(br) time | O(br) space
def apartmenbtHunting1(blocks,reqs):
	minDistFromBlocks = list(map(lambda req:getminDist(blocks,req),reqs))
	maxDistAtBlocks = getMaxDistAtBlocks(blocks,minDistFromBlocks)
	return getIdxAtMinValue(maxDistAtBlocks)

def getminDist(blocks,req):
	minDist = [0 for block in blocks]
	closestReqIdx = float('inf')
	for i in range(len(blocks)):
		if blocks[i][req]:
			closestReqIdx = i
			minDist[i] = distanceBetween(i,closestReqIdx)
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closestReqIdx = i
		minDist[i] = min(minDist[i],disanceBetween)
	return minDist

def getMaxDistAtBlocks(blocks,minDistFromBlocks):
	maxDistAtBlocks = [0 for blocks in blocks]
	for i in range(len(blocks)):
		minDistAtBlocks = list(map(lambda distances: distances[i],minDistFromBlocks))
		maxDistAtBlocks[i] = max(minDistAtBlocks)
	return maxDistAtBlocks

def getIdxAtMinValue(array):
	idxAtMinValue = 0
	minValue = float('inf')
	for i in range(len(array)):
		currentValue = array[i]
		if currentValue < minValue:
			minValue = currentValue
			idxAtMinValue = i
	return idxAtMinValue

def distanceBetween(a,b):
		return abs(a-b)