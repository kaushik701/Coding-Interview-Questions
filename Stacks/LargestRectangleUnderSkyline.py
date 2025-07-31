# O(n) time | O(1) space
def LargestRectangleUnderSkyline(buildings):
	maxArea = 0
	for idx in range(len(buildings)):
		currentHeight = buildings[idx]
		furthestLeft = idx
		while furthestLeft > 0 and buildings[furthestLeft - 1] >= currentHeight:
			furthestLeft -= 1
		furthestRight = idx
		while furthestRight < len(buildings) - 1 and buildings[furthestLeft + 1] >= currentHeight:
			furthestRight += 1
		areaWithCurrentBuilding = (furthestRight - furthestLeft + 1) * currentHeight
		maxArea = max(areaWithCurrentBuilding,maxArea)
	return maxArea

# O(n) time | O(n) space
def LargestRectangleUnderSkyline1(buildings):
	indices = []
	maxArea = 0
	for idx, height in enumerate(buildings+[0]):
		while len(indices) != 0 and buildings[indices[len(indices)-1]] >= height:
			pillarHeight = buildings[indices.pop()]
			width = idx if len(indices) == 0 else idx - indices[len(indices)-1] - 1
			maxArea = max(width*pillarHeight, maxArea)
		indices.append(idx)
	return maxArea

print(LargestRectangleUnderSkyline([1,3,3,2,4,1,5,3,2]))
print(LargestRectangleUnderSkyline1([1,3,3,2,4,1,5,3,2]))