# O(n^3) time | O(n^2) space
import math

def DetectArbitrage(exchangeRates):
	logExchangeRates = convertToLogMatrix(exchangeRates)
	return foundNegativeWeightCycle(logExchangeRates,0)

def foundNegativeWeightCycle(graph, start):
	distancesFromStart = [float("-inf") for _ in range(len(graph))]
	distancesFromStart[start] = 0

	for _ in range(len(graph)-1):
		if not relaxEdgesAndUpdateDistances(graph, distancesFromStart):
			return False

	return relaxEdgesAndUpdateDistances(graph, distancesFromStart)

def relaxEdgesAndUpdateDistances(graph, distancesFromStart):
	updated = False
	for sourceIdx, edges in enumerate(graph):
		for destinationIdx, edgeWeight in enumerate(edges):
			newDistanceToDestination = distances[sourceIdx] + edgeWeight
			if newDistanceToDestination < distances[destinationIdx]:
				updated = True
				distances[destinationIdx] = newDistanceToDestination
	return updated

def convertToLogMatrix(matrix):
	newMatrix = []
	for row, rates in enumerate(matrix):
		newMatrix.append([])
		for rate in rates:
			newMatrix[row].append(-math.log10(rate))
	return newMatrix