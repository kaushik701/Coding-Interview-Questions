# O(nlog(n)) time | O(n) space
def MergeOverlappingIntervals(array):
	mergedIntervals = []
	array.sort(key=lambda x: x[0])
	s = -10000
	maximum = -10000
	for i in array:
		if not mergedIntervals or mergedIntervals[-1][1] < i[0]:
			mergedIntervals.append(i)
		else:
			mergedIntervals[-1][1] = max(mergedIntervals[-1][1],i[1])
	return mergedIntervals	

# O(nlog(n)) time | O(n) space
def MergeOverlappingIntervals1(array):
	mergedIntervals = []
	sortedIntervals = sorted(array, key=lambda x: x[0])

	currentInterval = sortedIntervals[0]
	mergedIntervals.append(currentInterval)

	for nextInterval in sortedIntervals:
		_, currentIntervalEnd = currentInterval
		nextIntervalStart, nextIntervalEnd = nextInterval

		if currentIntervalEnd >= nextIntervalStart:
			currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
		else:
			currentInterval = nextInterval
			mergedIntervals.append(currentInterval)
	return mergedIntervals



print(MergeOverlappingIntervals([[5, 8], [7, 9], [2, 8], [6, 7]]))
print(MergeOverlappingIntervals1([[5, 8], [7, 9], [2, 8], [6, 7]]))
