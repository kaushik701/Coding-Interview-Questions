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

# O(n) time | O(k) space
HOME_TEAM_WON = 1

def TournamentWinner1(competitions, results):
	currentBestTeam = ""
	scores = {currentBestTeam:0}
	for idx, competition in enumerate(competitions):
		result = results[idx]
		homeTeam, awayTeam = competition

		winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

		updateScores(winningTeam,3, scores)

		if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam = winningTeam
	return currentBestTeam

def updateScores(team, points, scores):
	if team not in scores:
		scores[team] = 0

	scores[team] += points
