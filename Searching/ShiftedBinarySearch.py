# O(log(n)) time | O(log(n)) space
array = list(map(int,input('Enter the Numbers: ').split()))
target = int(input('Enter the Number: '))

def ShiftedBinarySearch(array,target):
	return ShiftedBinarySearchHelper(array,target,0,len(array)-1)

def ShiftedBinarySearchHelper(array,target,left,right):
	if left > right:
		return -1
	middle = (left+right) // 2
	potentialMatch = array[middle]
	leftNum = array[left]
	rightNum = array[right]
	if target == potentialMatch:
		return middle
	elif leftNum <= potentialMatch:
		if target < potentialMatch and target >= leftNum:
			return ShiftedBinarySearchHelper(array,target,left,middle-1)
		else:
			return ShiftedBinarySearchHelper(array,target,middle+1,right)
	else:
		if target > potentialMatch and target <= rightNum:
			return ShiftedBinarySearchHelper(array,target,middle+1,right)
		else:
			return ShiftedBinarySearchHelper(array,target,left,middle-1)

# O(log(n)) time | O(1) space
def ShiftedBinarySearch1(array,target):
	return ShiftedBinarySearchHelper1(array,target,0,len(array)-1)

def ShiftedBinarySearchHelper1(array,target,left,right):
	while left <= right:
		middle = (left+right) // 2
		potentialMatch = array[middle]
		leftNum = array[left]
		rightNum = array[right]
		if target == potentialMatch:
			return middle
		elif leftNum <= potentialMatch:
			if target < potentialMatch and target >= leftNum:
				right = middle-1
			else:
				left = middle + 1
		else:
			if target > potentialMatch and target <= rightNum:
				left = middle + 1
			else:
				right = middle - 1
	return -1

print(ShiftedBinarySearch(array,target))
print(ShiftedBinarySearch(array,target))