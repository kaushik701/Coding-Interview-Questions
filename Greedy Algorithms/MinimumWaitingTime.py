# O(nlog(n)) time | O(1) space
def MinimumWaitingTime(array):
	array.sort()
	totalWaitingTime = 0
	for idx, duration in enumerate(array):
		arrayLeft = len(array) - (idx+1)
		totalWaitingTime += duration * arrayLeft
	return totalWaitingTime

print(MinimumWaitingTime([3,2,1,2,6]))