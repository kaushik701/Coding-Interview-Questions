# O(nlog(n)) time | O(1) space
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

print(MergeOverlappingIntervals([[5, 8], [7, 9], [2, 8], [6, 7]]))