# O(log(n)) time | O(log(n)) space
array = list(map(int,input('Enter the Numbers: ').split()))
key = int(input('Enter the Key: '))

def BinarySearch(array,key):
	return BinarySearchHelper(array,key,0,len(array)-1)

def BinarySearchHelper(array,key,left,right):
	if left > right:
		return -1
	middle = (left+right) // 2
	potentialMatch  =array[middle]
	if key == potentialMatch:
		return middle
	elif key < potentialMatch:
		return BinarySearchHelper(array,key,left,middle-1)
	else:
		return BinarySearchHelper(array,key,middle+1,right)

# O(log(n)) time | O(1) space
def BinarySearch1(array,key):
	return BinarySearchHelper1(array,key,0,len(array)-1)

def BinarySearchHelper1(array,key,left,right):
	while left <= right:
		middle = (left+right) // 2
		potentialMatch  =array[middle]
		if key == potentialMatch:
			return middle
		elif key < potentialMatch:
			right = middle-1
		else:
			left = middle+1
	return -1

print(BinarySearch(array,key))
print(BinarySearch1(array,key))