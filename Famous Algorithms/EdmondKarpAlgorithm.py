# O(V*E^2) time | O(V) space
class Graph:
	def __init__(self,size):
		self.adjacentMatrix = [[0]*size for _ in range(size)]
		self.size = size
		self.vertexData = ['']*size

	def addEdge(self,u,v,weight):
			self.adjacentMatrix[u][v] = c

	def addVertexData(self,vertex,data):
		if 0 <= vertex < self.size:
			self.vertexData[vertex] = data

	def BreadthFirstSearch(self,s,t,parent):
		visited = [False]*self.size
		queue = []
		queue.append(s)
		visited[s] = True

		while queue:
			u = queue.pop(0) # Pop from the start of the list

			for ind,val in enumerate(self.adjacentMatrix[u]):
			if not visited[ind] and val > 0:
				queue.append(ind)
				visited[ind] = True
				parent[ind] = u

		return visited[t]

	def EdmondKarp(self,source,target):
		parent = [-1]*self.size
		maxFlow = 0

		while self.BreadthFirstSearch(source,target,parent):
			pathFlow = float("inf")
			s = target
			while s != source:
				pathFlow = min(pathFlow,self.adjacentMatrix[parent[s]][s])
				s = parent[s]

			maxFlow += pathFlow
			v = target
			while v != source:
				u = parent[v]
				self.adjacentMatrix[u][v] -= pathFlow
				self.adjacentMatrix[v][u] += pathFlow
				v = parent[v]
			path = []
			v = target
			while v != source:
				path.append(v)
				v = parent[v]
			path.append(source)
			path.reverse()
		return maxFlow