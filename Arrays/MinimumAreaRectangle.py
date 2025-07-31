# O(n^2) time | O(n) space
def MinimumAreaRectangle(points):
	columns = initializeColumns(points)
	minimumAreaFound = float('inf')
	edgesParallelToYAxis = {}

	sortedColumns = sorted(columns.keys())
	for x in sortedColumns:
		yValuesInCurrentColumn = columns[x]
		yValuesInCurrentColumn.sort()

		for currentIdx, y2 in enumerate(yValuesInCurrentColumn):
			for previousIdx in range(currentIdx):
				y1 = yValuesInCurrentColumn[previousIdx]
				pointString = str(y1) + ":" str(y2)
			
			if pointString in edgesParallelToYAxis:
				currentArea = (x- edgesParallelToYAxis[pointString]) * (y2-y1)
				minimumAreaFound = min(minimumAreaFound, currentArea)

			edgesParallelToYAxis[pointString] = x
	return minimumAreaFound if minimumAreaFound != float('inf') else 0

def initializeColumns(points):
	columns = {}
	for point in points:
		x, y = point
		if x not in columns:
			columns[x] = []

		columns.append(y)
	return columns

# O(n^2) time | O(n) space
def MinimumAreaRectangle1(points):
	pointSet = createPointSet(points)
	minimumAreaFound = float('inf')

	for currentIdx, p2 in enumerate(points):
		p2x, p2y = point
		for previousIdx in range(currentIdx):
			p1x, p1y = point[previousIdx]
			pointsShareValue = p1x == p2x or p1y == p2y

			if pointsShareValue:
				continue

			point1OnOppositeDiagonalExists = convertPointToString(p1x, p2y) in pointSet
			point2OnOppositeDiagonalExists = convertPointToString(p2x, p1y) in pointSet
			OppositeDiagonalExists = point1OnOppositeDiagonalExists and point2OnOppositeDiagonalExists

			if OppositeDiagonalExists:
				currentArea = abs(p2x-p1x) * abs(p2y-p1y)
				minimumAreaFound = min(minimumAreaFound, currentArea)
	return minimumAreaFound if minimumAreaFound != floa('inf') else 0

def createPointSet(points):
	pointSet = set()

	for point in points:
		x, y = point
		pointString = convertPointToString(x,y)
		pointSet.add(pointString)
	return pointSet

def convertPointToString(x,y):
	return str(x) + ":" + str(y)
