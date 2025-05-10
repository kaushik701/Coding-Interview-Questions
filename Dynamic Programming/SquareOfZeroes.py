# O(n^4) time | O(n^3) space
def squareOfZeroes(matrix):
	lastIdx = len(matrix) - 1
	return hasSquareOfZeroes(matrix,0,0,lastIdx,lastIdx,{})

def hasSquareOfZeroes(matrix, r1,c1,r2,c2,cache):
	if r1>= r2 or c1>= c2:
		return False
	key = str(r1) + "-" + str(c1) + "-" + str(r2) + "-" + str(c2)
	if key in cache:
		return cache[key]

	cache[key] = {
		isSquareOfZeroes(matrix,r1,c1,r2,c2)
		or hasSquareOfZeroes(matrix,r1+1,c1+1,r2-1,c2-1,cache)
		or hasSquareOfZeroes(matrix,r1, c1+1,r2-1,c2,cache)
		or hasSquareOfZeroes(matrix,r1+1,c1,r2,c2-1,cache)
		or hasSquareOfZeroes(matrix,r1+1,c1+1,r2,c2,cache)
		or hasSquareOfZeroes(matrix,r1,c1,r2-1,c2-1,cache)
	}
	return cache[key]

def isSquareOfZeroes(matrix,r1,c1,r2,c2):
	for row in range(r1,r2+1):
		if matrix[row][c1] != 0 or matrix[row][c2] != 0:
			return False
	for col in range(c1,c2+1):
		if matrix[r1][col] != 0 or matrix[r2][col] != 0:
			return False
	return True

# O(n^4) time | O(1) space
def squareOfZeroes1(matrix):
	n=len(matrix)
	for topRow in range(n):
		for leftCol in range(n):
			squareLength = 2
			while squareLength <= n - leftCol and squareLength <= n- topRow:
				bottomRow = topRow + squareLength - 1
				rightCol = leftCol - squareLength - 1
				if isSquareOfZeroes(matrix,topRow,leftCol,bottomRow,rightCol):
					return True
				squareLength += 1
	return False
