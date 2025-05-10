# O(n*d) time | O(n) space
def getNumberOfWaysToMakeChange(targetAmount,denoms):
	ways = [0 for amount in range(targetAmount+1)]
	ways[0] = 1
	for denom in denoms:
		for amount in range(1,targetAmount+1):
			if denom <= amount:
				ways[amount] += ways[amount-denom]
	return ways[targetAmount]

print(getNumberOfWaysToMakeChange(9,[1,2,5]))