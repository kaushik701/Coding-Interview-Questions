# O(n) time | O(n) space
array = list(map(int,input('Enter the Numbers: ').split()))
def FirstDuplicateValue(array):
	num_set = set()
	num_duplicate = 0
	for i in range(len(array)):
		if array[i] in num_set:
			return array[i]
		else:
			num_set.add(array[i])
	return num_duplicate

print(FirstDuplicateValue(array))