# O(k^n) time | O(n) space
def StaircaseTraversal(height, maxSteps):
	return numberOfWaysToTop(height, maxSteps)

def numberOfWaysToTop(height, maxSteps):
	if height <= 1:
		return 1
	numberOfWays = 0
	for step in range(1, min(maxSteps, height)+1):
		numberOfWays += numberOfWaysToTop(height-step, maxSteps)
	return numberOfWays

# O(n*k) time | O(n) space
def StaircaseTraversal1(height, maxSteps):
	return numberOfWaysToTop1(height, maxSteps, {0:1,1:1})

def numberOfWaysToTop1(height, maxSteps, memoize):
	if height in memoize:
		return memoize[height]
	numberOfWays = 0
	for step in range(1, min(maxSteps, height)+1):
		numberOfWays += numberOfWaysToTop(height-step, maxSteps)
	memoize[height] = numberOfWays 
	return numberOfWays

# O(n*k) time | O(n) space
def StaircaseTraversal2(height, maxSteps):
	waysToTop = [0 for _ in range(height+1)]

	waysToTop[0] = 1
	waysToTop[1] = 1

	for currentHeight in range(2, height+1):
		step = 1
		while step <= maxSteps and step <= currentHeight:
			waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight-step]
			step += 1
	return waysToTop[height]

# O(n) time | O(n) space
def StaircaseTraversal3(height, maxSteps):
	currentNumberOfWays = 0
	waysToTop = [1]

	for currentHeight in range(1, height+1):
		startOfWindow = currentHeight - maxSteps - 1
		endOfWindow = currentHeight - 1
		if startOfWindow >= 0:
			currentNumberOfWays -= waysToTop[startOfWindow]
		currentNumberOfWays += waysToTop[endOfWindow]
		waysToTop.append(currentNumberOfWays)
	return waysToTop[height]

print(StaircaseTraversal(4,2))
print(StaircaseTraversal1(4,2))
print(StaircaseTraversal2(4,2))
print(StaircaseTraversal3(4,2))