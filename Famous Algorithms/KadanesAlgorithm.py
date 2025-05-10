# O(n) time | O(1) space
array = list(map(int,input("Enter the numbers: ").split()))
def KadanesAlgorithm(array):
	maxEngingHere = array[0]
	maxSoFar = array[0]
	for num in array[1:]:
		maxEngingHere = max(num,maxEngingHere+num)
		maxSoFar = max(maxSoFar,maxEngingHere)
	return maxSoFar

print(KadanesAlgorithm(array))