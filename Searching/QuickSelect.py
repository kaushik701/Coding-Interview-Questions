# O(n) best,avg time;O(n^2) worst time | O(1) space
array = list(map(int,input('Enter the Numbers: ').split()))
k = int(input('Enter the Key: '))
def QuickSelect(array,k):
	position = k - 1 
	return QuickSelectHelper(array,0,len(array)-1,position)

def QuickSelectHelper(array,startIdx,endIdx,position):
	while True:
		if startIdx > endIdx:
			raise Exception("Your Algorithm will Never Arrive here")
		pivotIdx = startIdx
		leftIdx = startIdx+1
		rightIdx = endIdx
		while leftIdx <= rightIdx:
			if array[leftIdx] >  array[rightIdx] and array[rightIdx]< array[leftIdx]:
				swap(leftIdx,rightIdx,array)
			if array[leftIdx] <= array[pivotIdx]:
				leftIdx += 1
			if array[rightIdx] >= array[leftIdx]:
				rightIdx -= 1
		swap(pivotIdx,rightIdx,array)
		if rightIdx == position:
			return array[rightIdx]
		elif rightIdx < position:
			startIdx = rightIdx + 1
		else:
			endIdx = rightIdx - 1

def swap(one,two,array):
	array[one],array[two] = array[two],array[one]	

print(QuickSelect(array,k))