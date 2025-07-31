# O(n) time | O(n) space
array = list(map(int,input('Enter the Numbers: ').split()))
def FirstDuplicateValue(array):
	numberSet = set()
	numberDuplicate = 0
	for i in range(len(array)):
		if array[i] in numberSet:
			return array[i]
		else:
			numberSet.add(array[i])
	return numberDuplicate

# O(n^2) time | O(1) space
def FirstDuplicateValue1(array):
	minimumSecondIndex = len(array)
	for i in range(len(array)):
		value = array[i]
		for j in range(i+1, len(array)):
			valueToCompare = array[j]
			if value == valueToCompare:
				minimumSecondIndex = min(minimumSecondIndex, j)

	if minimumSecondIndex == len(array):
		return -1

	return array[minimumSecondIndex]

# O(n) time | O(n) space
def FirstDuplicateValue2(array):
	seen = set()
	for value in array:
		if value in seen:
			return value
		seen.add(value)
	return -1

# O(n) time | O(1) space
def FirstDuplicateValue3(array):
	for value in array:
		if array[abs(value)-1] < 0:
			return abs(value)
		array[abs(value)-1] *= -1
	return -1

print(FirstDuplicateValue(array))
print(FirstDuplicateValue1(array))
print(FirstDuplicateValue2(array))
print(FirstDuplicateValue3(array))