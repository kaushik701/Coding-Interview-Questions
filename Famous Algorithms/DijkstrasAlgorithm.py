# O(V^2 + E) time | O(V) space
def DijkstrasAlgorithm(start,edges):
    numberOfVertices = len(edges)

    minDistances = [float('inf') for _ in range(numberOfVertices)]
    minDistances[start] = 0

    visited = set()
 
    while len(visited) != numberOfVertices:
        vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)

        if currentMinDistance == float('inf'):
            break

        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            if destination in visited:
                continue

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance

    return list(map(lambda x:-1 if x == float('inf') else x, minDistances))


def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float('inf')
    vertex = None

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance

    return vertex, currentMinDistance


# O((V+E)*log(V)) time | O(V) space
def DijkstrasAlgorithm1():
    numberOfVertices = len(edges)

    minDistances = [float('inf') for _ in range(numberOfVertices)]
    minDistances[start] = 0

    minDistancesHeap = MinHeap([(idx, float('inf')) for idx in range(numberOfVertices)])
    minDistancesHeap.update(start,0)

    visited = set()

    while not minDistancesHeap.isEmpty():
        vertex, currentMinDistance = minDistancesHeap.remove()

        if vertex in visited:
            continue

        if currentMinDistance == float('inf'):
            break

        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            if destination in visited:
                continue

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
                minDistancesHeap.update(destination, newPathDistance)

    return list(map(lambda x:-1 if x == float('inf') else x, minDistances))

class MinHeap:
    def __init__(self,comparisonFunc,array):
        self.heap = self.buildHeap(array)
        self.comparisonFunc = comparisonFunc
        self.vertexMap = {idx:idx for idx in range(len(array))}

    # O(n) time  | O(1) space   
    def buildHeap(self,array):
        firstParentIdx = (len(array)-2) // 2
        for currentIdx in reversed(range(firstParentIdx)):
            self.shiftdown(currentIdx,len(array)-1, array)
        return array

    # O(log(n)) time | O(n) space
    def shiftDown(self,currentIdx,endIdx,heap):
        childOneIdx = currentIdx*2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != 1:
                if self.comparisonFunc(heap[childTwoIdx][1],heap[childOneIdx][1]):
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
            else:
                idxToSwap = childOneIdx
            if self.comparisonFunc(heap[idxToSwap],heap[currentIdx]):
                self.swap(currentIdx,idxToSwap,heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break

    # O(log(n)) time | O(n) space
    def shiftUp(self,currentIdx,heap):
        parentIdx = (currentIdx-1) // 2
        while currentIdx > 0:
            if self.comparisonFunc(heap[currentIdx][1],heap[parentIdx][1 ]):
                self.swap(currentIdx,parentIdx,heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx-1) // 2
            else:
                return

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    def isEmpty(self):
        return len(self.heap) == 0

    # O(log(n)) time | O(1) space
    def remove(self):
        swap(0, self.length-1,self.heap)
        vertex, distance = self.heap.pop()
        self.vertexMap.pop(vertex)
        self.shiftDown(0,self.length - 1, self.heap)
        return valueToRemove

    # O(log(n)) time | O(1) space
    def swap(self,i,j,heap):
        self.vertexMap[heap[i][0]] = j
        self.vertexMap[heap[j][0]] = i
        heap[i],heap[j] = heap[j],heap[i]

    def update(self,vertex, value):
    self.heap[self.vertexMap[vertex]] = (vertex, value)
    self.shiftUp(self.vertexMap[vertex], self.heap) 