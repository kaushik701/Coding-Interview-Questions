# O(V^2) time | O(V) space
class Graph:
	def __init__(self,size):
		self.adjacentMatrix = [[0]* size for _ in range(size)]
		self.size = size
		self.vertexData = ['']*size

	def addEdge(self,u,v,weight):
		if 0<= u < self.size and 0<= v < self.size:
			self.adjacentMatrix[u][v] = weight
			self.adjacentMatrix[v][u] = weight

	def addVertexData(self,vertex,data):
		if 0 <= vertex < self.size:
			self.vertexData[vertex] = data

	def PrimsAlgorithm(self):
		inMST = [False] * self.size
		keyValues = [float('inf')] * self.size
		parents = [-1] * self.size

		keyValues[0] = 0
		for _ in range(size):
			u = min((v for v in range(size) if not inMST[v]),key=lambda v:keyValues[v])
			inMST[u] = True
			for v in range(size):
				if 0 < self.adjacentMatrix[u][v] < keyValues[v] and not inMST[v]:
					keyValues[v] = self.adjacentMatrix[u][v]
					parents[v] = u
