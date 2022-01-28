# O(n) time | O(n) space
def zigzagTraverse(array):
	height = len(array) -1
	width = len(array[0]) - 1
	result = []
	row = 0
	col = 0
	goingDown = True
	while not isOutOfBounds(row,col,height,width):
		result.append(array[row][col])
		if goingDown:
			if col == 0 or row == height:
				goingDown = False
				if row == height:
					col += 1
				else:
					row += 1
			else:
				row += 1
				col -= 1
		else:
			if row == 0 or col == width:
				goingDown = True
				if col == width:
					row += 1
				else:
					col += 1
			else:
				row -= 1
				col += 1
	return result

def isOutOfBounds(row,col,height,width):
	return row < 0 or row > height or col < 0 or col > width

print(zigzagTraverse([[11, 12, 5, 2], 
					  [15, 6, 10,13], 
					  [17, 8, 16, 5], 
					  [7, 18, 19, 4]]))