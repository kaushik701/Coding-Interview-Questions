# Leetcode #36: https://youtu.be/TjFXEUCMqI8?si=A0zWGd-k0KPP7B84
# O(n) time | O(1) space
import collections
def validSudoku(board):
	cols = collections.defaultdict(set)
	rows = collections.defaultdict(set)
	squares = collections.defaultdict(set)

	for r in range(9):
		for c in range(9):
			if board[r][c] == " ":
				continue
			if (board[r][c] in rows[r] or
				board[r][c] in cols[c] or
				board[r][c] in squares[(r//3,c//3)]):
				return False
			cols[c].add(board[r][c])
			rows[r].add(board[r][c])
			squares[(r//3,c//3)].add(board[r][c])
	return True