# O(n^2) avg time | O(n^2) space
array = list(map(int,input('Enter the Numbers: ').split()))
targetSum = int(input('Enter the number: '))
def fournumbersum(array,targetSum):
	allPairSums = {}
	quadruplets = []
	for i in range(1,len(array)-1):
		for j in range(i+1,len(array)):
			currentSum = array[i] + array[j]
			difference = targetSum - currentSum
			if difference in allPairSums:
				for pair in allPairSums[difference]:
					quadruplets.append(pair+[array[i],array[j]])
		for k in range(0,i):
			currentSum = array[i] + array[k]
			if currentSum not in allPairSums:
				allPairSums[currentSum] = [[array[k],array[i]]]
			else:
				allPairSums[currentSum].append([array[k],array[i]])
	return quadruplets

print(fournumbersum(array,targetSum))