# O(E.f) time | O(V) space
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

	def DepthFirstSearch(self,s,t,visited=None,path=None):
		if visited is None:
			visited = [False]*self.size
		if path is None:
			path = []

		visited[s] = True
		path.append(s)

		if s == t:
			return path

		for ind, val in enumerate(self.adjacentMatrix[s]):
			if not visited[ind] and val > 0:
				resultPath = self.DepthFirstSearch(ind,t,visited,path.copy())
				if resultPath:
					return resultPath
		return None

	def FordFulkerson(self,source,target):
		maxFlow = 0
		path = self.DepthFirstSearch(source,target)
		while path:
			pathFlow = float("inf")
			for i in range(len(path)-1):
				u,v = path[i],path[i+1]
				pathFlow = min(pathFlow,self.adjacentMatrix[u][v])

			for i in range(len(path)-1):
				u,v = path[i],path[i+1]
				self.adjacentMatrix[u][v] -= pathFlow
				self.adjacentMatrix[v][u] += pathFlow
			maxFlow += pathFlow
			path = self.DepthFirstSearch(source,target)

		return maxFlow