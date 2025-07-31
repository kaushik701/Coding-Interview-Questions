# O(1) time | O(1) space
def SolveSudoku(board):
	SolvePartialSudoku(0,0, board)
	return board

def SolvePartialSudoku(row,col,board):
	currentRow = row
	currentCol = col

	if currentCol == len(board[row]):
		currentRow += 1
		currentCol = 0
		if currentRow == len(board):
			return True

	if board[currentRow][currentCol] == 0:
		return tryDigitsAtPosition(currentRow, currentCol, board)

	return SolvePartialSudoku(currentRow, currentCol+1, board)

def tryDigitsAtPosition(row, col, board):
	for digit in range(1,10):
		if isValidAtPosition(digit,row,col,board):
			board[row][col] = digit
			if SolvePartialSudoku(row, col+1, board):
				return True
	board[row][col] = 0
	return False
	
def isValidAtPosition(value, row, col, board):
	rowIsValid = value not in board[row]
	colIsValid = value not in map(lambda r: r[col], board)

	if not rowIsValid or not colIsValid:
		return False

	subGridRowStart = row // 3
	subGridColStart = col // 3
	for rowIdx in range(3):
		for colIdx in range(3):
			rowToCheck = subGridRowStart * 3 + rowIdx
			colToCheck = subGridColStart * 3 + colIdx
			existingValue = board[rowToCheck][colToCheck]

			if existingValue == value:
				return False
	return True