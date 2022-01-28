# O(n^2) worst time, O(nlog(n)) best time, O(nlog(n)) avg time| O(log(n)) space
array = list(map(int,input('Enter the Numbers: ').split()))
def QuickSort(array):
	QuickSortHelper(array,0,len(array)-1)
	return array

def QuickSortHelper(array,startIdx,endIdx):
	if startIdx >= endIdx:
		return 
	pivotIdx = startIdx
	leftIdx = startIdx+1
	rightIdx = endIdx
	while rightIdx >= leftIdx:
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			swap(leftIdx,rightIdx,array)
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1
	swap(pivotIdx,rightIdx,array)
	leftSubarrayIsSmaller = rightIdx -1 - startIdx < endIdx - (rightIdx+1)
	if leftSubarrayIsSmaller:
		QuickSortHelper(array,startIdx,rightIdx-1)
		QuickSortHelper(array,rightIdx+1,endIdx)
	else:
		QuickSortHelper(array,rightIdx+1,endIdx)
		QuickSortHelper(array,startIdx,rightIdx-1)

def swap(i,j,array):
	array[i],array[j] = array[j],array[i]

print(QuickSort(array))