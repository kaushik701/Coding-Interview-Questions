# O(n^2) time |O(n^2) space
def rectangleMania(coords):
	coordsTable = getCoordsTable(coords)
	return getRectangleCount(coords,coordsTable)

def getCoordsTable(coords):
	coordsTable = {}
	for coord1 in coords:
		coord1Directions = {
			UP:[], RIGHT:[], DOWN:[], LEFT:[]
		}
		for coord2 in coords:
			coord2Direction = getCoordDirection(coord1,coord2)
			if coord2Direction in coord1Directions:
				coord1Directions[coord2Direction].append(coord2)
		coord1String = coordToString(coord1)
		coordsTable[coord1String] = coord1Directions
	return coordsTable

def getCoordDirection(coord1,coord2):
	x1,y1 = coord1
	x2,y2 = coord2
	if y2 == y1:
		if x2 > x1:
			return RIGHT
		elif x2 < x1:
			return LEFT
	elif x2 == x1:
		if y2 > y1:
			return UP
		elif y2 < y1:
			return DOWN
	return " "

def getRectangleCount(coords,coordsTable):
	rectangleCount = 0
	for coord in coords:
		rectangleCount += clockwiseCountRectangles(coord,coordsTable,UP,coord)
	return rectangleCount

def clockwiseCountRectangles(coord, coordsTable, direction, origin):
	coordString = coordToString(coord)
	if direction == LEFT:
		rectangleFound = origin in coordsTable[coordString][LEFT]
		return 1 if rectangleFound else 0
	else:
		rectangleCount = 0
		nextDirection = getNextClockwiseDirection(direction)
		for nextCoord in coordsTable[coordString][direction]:
			rectangleCount += clockwiseCountRectangles(nextCoord,coordsTable, nextDirection,origin)
		return rectangleCount

def getNextClockwiseDirection(direction):
	if direction == UP:
		return RIGHT
	if direction ==  RIGHT:
		return DOWN
	if direction ==  DOWN:
		return LEFT
	return ''

def coordToString(coord):
	x,y = coord
	return str(x) + '-' + str(y)
	

# O(n^2) time | O(n) space
def rectangleMania2(coords):
	coordsTable = getCoordsTable2(coords)
	return getRectangleCount2(coords,coordsTable)

def getCoordsTable2(coords):
	coordsTable = {'x':{},'y':{}}
	for coord in coords:
		x,y = coord
		if x not in coordsTable['x']:
			coordsTable['x'][x] = []
		coordsTable['x'][x].append(coord)
		if y not in coordsTable['y']:
			coordsTable['y'][y] = []
		coordsTable['y'][y].append(coord)
	return coordsTable

def getRectangleCount2(coords,coordsTable):
	rectangleCount = 0
	for coord in coords:
		lowerLeftY = coord[1]
		rectangleCount += clockwiseCountRectangles2(coords,coordsTable,UP,lowerLeftY)
	return rectangleCount

def clockwiseCountRectangles2(coord1,coordsTable,direction,lowerLeftY):
	x1,y1 = coord1
	if direction == DOWN:
		releventCoords = coordsTable['x'][x1]
		for coord2 in releventCoords:
			lowerRightY = coord2[1]
			if lowerRightY ==  lowerLeftY:
				return 1
		return 0
	else:
		rectangleCount = 0
		if direction == UP:
			releventCoords = coordsTable['x'][x1]
			for coord2 in releventCoords:
				y2 = coord2[1]
				isAbove = y2>y1
				if isAbove:
					rectangleCount += clockwiseCountRectangles2(coord2,coordsTable,RIGHT,lowerLeftY)
		elif direction == RIGHT:
			releventCoords = coordsTable['y'][y1]
			for coord2 in releventCoords:
				x2 = coord2[1]
				isRight = x2>x1
				if isRight:
					rectangleCount += clockwiseCountRectangles2(coord2,coordsTable,DOWN,lowerLeftY)
		return rectangleCount

# O(n^2) time | O(n) space
def rectangleMania3(coords):
	coordsTable = getCoordsTable3(coords)
	return getRectangleCount3(coords,coordsTable)

def getCoordsTable(coords):
	coordsTable = {}
	for coord in coords:
		coordString = coordToString2(coord)
		coordsTable[coordString] = True
	return coordsTable

def getRectangleCount3(coords,coordsTable):
	rectangleCount = 0
	for x1,y1 in coords:
		for x2,y2 in coords:
			if not isInUpperRight([x1,y1],[x2,y2]):
				continue
			upperCoordString = coordToString([x1,y2])
			rightCoordString = coordToString([x2,y1])
			if upperCoordString in coordsTable and rightCoordString in coordsTable:
				rectangleCount += 1
	return rectangleCount

def isInUpperRight(coord1,coord2):
	x1,y1 = coord1
	x2,y2 = coord2
	return x2 > x1 and y2 > y1

def coordToString2(coord):
	x,y = coord
	return str(x) + '-' + str(y)

UP = 'up'
RIGHT = 'right'
DOWN = 'down'
LEFT = 'left'