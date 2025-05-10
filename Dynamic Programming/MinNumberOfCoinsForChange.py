# O(n*d) time | O(n) space
def getMinNumberOfCoinsForChange(targetAmount,denoms):
	numOfCoins = [float("inf") for amount in range(targetAmount+1)]
	numOfCoins[0] = 0
	for denom in denoms:
		for amount in range(len(numOfCoins)):
			if denom <= amount:
				numOfCoins[amount] = min(numOfCoins[amount],1+numOfCoins[amount-denom])
	return numOfCoins[targetAmount] if numOfCoins[targetAmount] != float("inf") else -1

print(getMinNumberOfCoinsForChange(17,[3,6]))