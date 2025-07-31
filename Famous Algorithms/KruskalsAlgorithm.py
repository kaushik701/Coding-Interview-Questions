# O(nlogn) time | O(n) space
class Graph:
	def __init__(self,size):
		self.edges = [] # storing edges as (weight,u,v)
		self.size = size
		self.vertexData = ['']*size

	def addEdge(self,u,v,weight):
		if 0<= u < self.size and 0<= v < self.size:
			self.edges.append((u,v,weight))

	def addVertexData(self,vertex,data):
		if 0 <= vertex < self.size:
			self.vertexData[vertex] = data

	def find(self,parent,i):
		if parent[i] == i:
			return i
		return self.find(parent,parent[i])

	def union(self,parent,rank,x,y):
		xroot = self.find(parent,x)
		yroot = self.find(parent,y)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	def kruskalsAlgorithm(self):
		result = [] #MST
		i=0 # edge counter

		self.edges = sorted(self.edges,key=lambda item: item[2])
		parent,rank = [],[]
		
		for node in range(self.size):
			parent.append(node)
			rank.append(0)

		while i < len(self.edges):
			u,v,weight = self.edges[i]
			i += 1

			x = self.find(parent,u)
			y = self.find(parent,v)

			if x != y:
				result.append((u,v,weight))
				self.union(parent,rank,x,y)