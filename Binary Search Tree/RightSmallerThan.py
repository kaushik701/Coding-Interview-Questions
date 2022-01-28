# O(n^2) time | O(n) space
def RightSmallerThan(array):
	RightSmallerCounts = []
	for i in range(len(array)):
		RightSmallerCount = 0
		for j in range(i+1,len(array)):
			if array[j] < array[i]:
				RightSmallerCount += 1
		RightSmallerCounts.append(RightSmallerCount)
	return RightSmallerCounts

# O(nlog(n)) time | O(n) space
"""def RightSmallerThan1(array):
	if len(array) == 0:
		return []
	lastIdx = len(array) - 1
	bst = SpecialBST(array[lastIdx],lastIdx,0)
	for idx in reversed(range(len(array)-1)):
		bst.insert(array[idx],idx,0)
    rightSmallerCounts = array[:]
    getRightSmallerCounts(bst, rightSmallerCounts)
    return rightSmallerCounts

def getRightSmallerCounts(bst, rightSmallerCounts):
    if bst is None:
        return
    rightSmallerCounts[bst.idx] = bst.numSmallerAtInsertTime
    getRightSmallerCounts(bst.left, rightSmallerCounts)
    getRightSmallerCounts(bst.right, rightSmallerCounts)

class SpecialBST:
    def __init__(self,value,idx,numSmallerAtInsertTime):
        self.value = value
        self.idx = idx
        self.left = None
        self.right = None
        self.numSmallerAtInsertTime= numSmallerAtInsertTime
        self.leftSubTreeSize=0

    def insert(self,val,idx,numSmallerAtInsertTime):
        if self.value < val:
            numSmallerAtInsertTime+=self.leftSubTreeSize
            if val > self.value:
                numSmallerAtInsertTime+=1
            if self.right is None:
                self.right = SpecialBST(val,idx,numSmallerAtInsertTime)
            else:
                self.right.insert(val,idx,numSmallerAtInsertTime)
        else:
            self.leftSubTreeSize += 1
            if self.left is None:
                self.left = SpecialBST(val,idx,numSmallerAtInsertTime)
            else:
                self.left.insert(val, idx, numSmallerAtInsertTime)
"""
print(RightSmallerThan([8,5,11,1,3,6,4]))
#print(RightSmallerThan1([8,5,11,1,3,6,4]))     