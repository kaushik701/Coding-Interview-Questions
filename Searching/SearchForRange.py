# O(log(n)) time | O(log(n)) space
array = list(map(int,input('Enter the Numbers: ').split()))
target = int(input('Enter the Target: '))
def SearchForRange(array,target):
	finalRange = [-1,-1]
	alteredBinarySearch(array,target,0,len(array)-1,finalRange,True)
	alteredBinarySearch(array,target,0,len(array)-1,finalRange,False)
	return finalRange

def alteredBinarySearch(array,target,left,right,finalRange,goleft):
	if left > right:
		return None
	middle = (left+right) // 2
	if array[middle] < target:
		alteredBinarySearch(array,target,middle+1,right,finalRange,goleft)
	elif array[middle] > target:
		alteredBinarySearch(array,target,left,middle-1,finalRange,goleft)
	else:
		if goleft:
			if middle == 0 or array[middle-1] != target:
				finalRange[0] = middle
			else:
				alteredBinarySearch(array,target,left,middle-1,finalRange,goleft)
		else:
			if middle == len(array)-1 or array[middle+1] != target:
				finalRange[1] = middle
			else:
				alteredBinarySearch(array,target,middle+1,right,finalRange,goleft)

# O(log(n)) time | O(1) space
def SearchForRange1(array,target):
	finalRange = [-1,-1]
	alteredBinarySearch1(array,target,0,len(array)-1,finalRange,True)
	alteredBinarySearch1(array,target,0,len(array)-1,finalRange,False)
	return finalRange

def alteredBinarySearch1(array,target,left,right,finalRange,goleft):
	while left <= right:
		middle = (left+right) // 2
		if array[middle] < target:
			left = middle+1
		elif array[middle] > target:
			right = middle-1
		else:
			if goleft:
				if middle == 0 or array[middle-1] != target:
					finalRange[0] = middle
					return 
				else:
					right = middle-1
			else:
				if middle == len(array)-1 or array[middle+1] != target:
					finalRange[1] = middle
					return
				else:
					left = middle+1

print(SearchForRange1(array,target))
print(SearchForRange(array,target))