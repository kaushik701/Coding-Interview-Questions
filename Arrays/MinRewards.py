# O(n^2) time | O(n) space
scores = list(map(int,input('Enter the Numbers: ').split()))
def minRewards(scores):
	rewards = [1 for _ in scores]
	for i in range(1,len(scores)):
		j = i-1
		if scores[i] > scores[j]:
			rewards[i] = rewards[j] + 1
		else:
			while j >= 0 and scores[j] > scores[j+1]:
				rewards[j] = max(rewards[j],rewards[j+1]+1)
				j -= 1
	return sum(rewards)

print(minRewards(scores))

# O(n) time | O(n) space
"""def minRewards1(scores):
	rewards = [1 for _ in scores]
	localminIdxs = getLocalMinIdxs(scores)
	for localminIdx in localminIdxs:
		expandFromLocalMinIdx(localminIdx,scores,rewards)
	return sum(rewards)

def getLocalMinIdxs(scores):
	if len(scores) == 1:
		return [0]
	localminIdxs = []
	for i in range(len(scores)):
		if i == 0 and scores[i] < scores[i+1]:
			localminIdxs.append(i)
		if i == len(scores) -1 and scores[i] < scores[i-1]:
			localminIdxs.append(i)
		if i == 0 or i == len(scores) -1:
			continue
		if scores[i] < scores[i+1] and scores[i] < scores[i-1]:
			localminIdxs.append(i)
	return localminIdxs


def expandFromLocalMinIdx(localminIdx,scores,rewards):
	leftIdx = localminIdx -1
	while leftIdx >=0 and scores[leftIdx] > scores[leftIdx+1]:
		rewards[leftIdx] = max(rewards[leftIdx],rewards[leftIdx+1]+1)
		leftIdx -= 1
	rightIdx = localminIdx +1
	while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx-1]:
		rewards[rightIdx] = rewards[rightIdx-1] + 1

print(minRewards1(scores))"""

# O(n) time | O(n) space
def minRewards2(scores):
	rewards = [1 for _ in scores]
	for i in range(1,len(scores)):
		if scores[i] > scores[i-1]:
			rewards[i] = rewards[i-1] + 1 
	for i in reversed(range(len(scores)-1)):
		if scores[i] > scores[i+1]:
			rewards[i] = max(rewards[i],rewards[i+1]+1)
	return sum(rewards)

print(minRewards2(scores))
