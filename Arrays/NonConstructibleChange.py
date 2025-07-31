# O(s*n) time | O(s*n) space
coins = list(map(int,input('Enter the Numbers: ').split()))
amount = int(input('Enter the Amount: '))

def NonConstructibleChange(coins,amount):
	dp = [float('inf')] * (amount+1)
	dp[0] = 0
	for coin in coins:
		for i in range(coin,amount+1):
			dp[i] = min(dp[i],dp[i-coin]+1)
	return dp[amount] if dp[amount] != float('inf') else -1

# O(nlog(n)) time | O(1) space
def NonConstructibleChange1(coins):
	coins.sort()

	currentChangeCreated = 0
	for coin in coins:
		if coin > currentChangeCreated + 1:
			return currentChangeCreated + 1
		currentChangeCreated += coin
	return currentChangeCreated + 1

print(NonConstructibleChange(coins,amount))
print(NonConstructibleChange1(coins))