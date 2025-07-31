# Leetcode #746: https://youtu.be/ktmzAZWkEZ0?si=9jSsAJUtVmVFA0o-
# O(n) time | O(1) space
def MinCostClimbingStairs(cost):
	cost.append(0)
	for i in range(len(cost)-3,-1,-1):
		cost[i] += min(cost[i+1],cost[i+2])
	return min(cost[0],cost[1])

print(MinCostClimbingStairs([10,15,20]))