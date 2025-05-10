# O(a*(a+r)+a+r+alog(a)) time | O(a+r) space: a-vertices, r-edges
def airportConnections(airports,routes,startingAirport):
	airportGraph = createAirportGraph(airports,routes)
	unreachableAirportNodes = getUnreachableAirportNodes(airportGraph,airports,startingAirport)
	markUnreachableConnections(airportGraph,unreachableAirportNodes)
	return getMinNumberOfNewConnections(airportGraph,unreachableAirportNodes)

# O(a+r) time | O(a+r) space
def createAirportGraph(airports,routes):
	airportGraph = {}
	for airport in airports:
		airportGraph[airport] = AirportNode(airport)
	for route in routes:
		airport, connection = route
		airportGraph[airport].connections.append(connection)
	return airportGraph

# O(a+r) time | O(a) space
def getUnreachableAirportNodes(airportGraph,airports,startingAirport):
	visitedAirports = {}
	depthFirstTraverseAirports(airportGraph,startingAirport,visitedAirports)

	unreachableAirportNodes = []
	for airport in airports:
		if airport in visitedAirports:
			continue
		airportNode = airportGraph[airport]
		airportNode.isReachable = False
		unreachableAirportNodes.append(airportNode)
	return unreachableAirportNodes

def depthFirstTraverseAirports(airportGraph,startingAirport,visitedAirports):
	if airport in visitedAirports:
		return
	visitedAirports[airport] = True
	connections = airportGraph[airport].connections
	for connection in connections:
		depthFirstTraverseAirports(airportGraph,visitedAirports,connection)

# O(a*(a+r)) time | O(a) space
def markUnreachableConnections(airportGraph,unreachableAirportNodes):
	for airportNode in unreachableAirportNodes:
		airport = airportNode.airport
		unreachableConnections = []
		depthFirstAddUnreachableConnections(airportGraph,airport,unreachableConnections,{})
		airportNode.unreachableConnections = unreachableConnections

def depthFirstAddUnreachableConnections(airportGraph,airport,unreachableConnections,visitedAirports):
	if airportGraph[airport].isReachable:
		return
	if airport in visitedAirports:
		return
	visitedAirports[airport] = True
	unreachableConnections.append(airport)
	connections = airportGraph[airport].connections
	for connection in connections:
		depthFirstAddUnreachableConnections(airportGraph,connection,unreachableConnections,visitedAirports)

# O(alog(a)+a+r) time | O(1) space
def getMinNumberOfNewConnections(airportGraph,unreachableAirportNodes):
	unreachableAirportNodes.sort(key = lambda airport: len(airport.unreachableConnections),reverse=True)
	numberofNewConnections = 0
	for airportNode in unreachableAirportNodes:
		if airportNode.isReachable:
			continue
		numberofNewConnections += 1
		for connection in airportNode.unreachableConnections:
			airportGraph[connection].isReachable = True
	return numberofNewConnections

class AirportNode:
	def __init__(self,airport):
		self.airport = airport
		self.connections = []
		self.isReachable = True
		self.unreachableConnections = []