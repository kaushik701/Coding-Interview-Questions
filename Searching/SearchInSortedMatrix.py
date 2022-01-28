# O(n+m) time | O(1) space n,m:-len(rows,cols) of matrix
def SearchInSortedMatrix(matrix,target):
	row = 0
	col = len(matrix[0])-1
	while row < len(matrix) and col >= 0:
		if matrix[row][col] > target:
			col -= 1
		elif matrix[row][col] < target:
			row += 1
		else:
			return [row,col]
	return [-1,-1]

print(SearchInSortedMatrix([
							[1,5,6,7],
							[11,15,16,18],
							[20,21,24,25],
							[26,27,29,30]
							],20))