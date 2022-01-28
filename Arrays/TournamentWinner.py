# O(n) time | O(1) space
n = int(input('Enter the Numbers: '))
def TournamentWinner(n):
	winners = 0
	while n != 1:
		if n%2 == 0:
			winners += n/2
			n = n/2
		else:
			winners += (n-1)/2
			n = 1 + (n-1)/2
	return round(winners)

# O(1) time | O(1) space
def TournamentWinner1(n):
	return n-1

print(TournamentWinner(n))
print(TournamentWinner1(n))