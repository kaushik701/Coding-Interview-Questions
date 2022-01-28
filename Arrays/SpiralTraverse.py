# O(n) time | O(n) space
def Spiraltraverse(array):
	result = []
	startRow = 0  
	endRow= len(array)-1
	startCol = 0
	endCol = len(array[0])-1

	while startRow <= endRow and startCol <= endCol:
		for col in range(startCol,endCol+1):
			result.append(array[startRow][col])

		for row in range(startRow+1,endRow+1):
			result.append(array[row][endCol])

		for col in reversed(range(startCol,endCol)):
			result.append(array[endRow][col])

		for row in reversed(range(startRow+1,endRow)):
			result.append(array[row][startCol])

		startRow += 1
		endRow -= 1
		startCol += 1
		endCol -= 1

	return result

print(Spiraltraverse([[11, 12, 5, 2], 
					  [15, 6, 10,13], 
					  [17, 8, 16, 5], 
					  [7, 18, 19, 4]]))

# O(n) time | O(n) space
def Spiraltraverse1(array):
	result = []
	spiralFill(array,0,len(array)-1,0,len(array[0])-1,result)
	return result

def spiralFill(array,startRow,endRow,startCol,endCol,result):
	if startRow > endRow or startCol > endCol:
		return  result

	for col in range(startCol,endCol+1):
		result.append(array[startRow][col])

	for row in range(startRow+1,endRow+1):
		result.append(array[row][endCol])

	for col in reversed(range(startCol,endCol)):
		result.append(array[endRow][col])

	for row in reversed(range(startRow+1,endRow)):
		result.append(array[row][startCol])

	spiralFill(array,startRow+1,endRow-1,startCol+1,endCol-1,result)

print(Spiraltraverse1([[11, 12, 5, 2], 
					  [15, 6, 10,13], 
					  [17, 8, 16, 5], 
					  [7, 18, 19, 4]]))
