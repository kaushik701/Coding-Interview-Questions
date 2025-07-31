# O(2^(n+m)) time | O(n+m) space
def NumberOfWaysToTraverseGraph(width, height):
	if width == 1 or height == 1:
		return 1
	return NumberOfWaysToTraverseGraph(width-1, height) + NumberOfWaysToTraverseGraph(width,height-1)

# O(n*m) time | O(n*m) space
def NumberOfWaysToTraverseGraph1(width, height):
	numberOfWays = [[0 for _ in range(width+1)]for _ in range(height+1)]
	for widthIdx in range(1, width+1):
		for heightIdx in range(1, height+1):
			if widthIdx == 1 or heightIdx == 1:
				numberOfWays[heightIdx][widthIdx] = 1
			else:
				waysLeft = numberOfWays[heightIdx][widthIdx-1]
				waysUp = numberOfWays[heightIdx-1][widthIdx]
				numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp

	return numberOfWays[height][width]

# O(n+m) time | O(1) space
def NumberOfWaysToTraverseGraph2(width, height):
	xDistanceToCorner = width - 1
	yDistanceTocorner = height - 1

	numerator = factorial(xDistanceToCorner + yDistanceTocorner)
	denominator = factorial(xDistanceToCorner) * factorial(yDistanceTocorner)
	return numerator // denominator

def factorial(num):
	result = 1
	for n in range(2, num+1):
		result *= n
	return result

print(NumberOfWaysToTraverseGraph(4,3))
print(NumberOfWaysToTraverseGraph1(4,3))
print(NumberOfWaysToTraverseGraph2(4,3))