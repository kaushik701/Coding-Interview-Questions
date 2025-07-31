# O(low*high*n) time | O(low*high) space
def AmbiguousMeasurements(measuringCups,low,high):
	memoization = {}
	return canMeasureInRange(measuringCups, low, high, memoization)

def canMeasureInRange(measuringCups, low, high, memoization):
	memoizeKey = createHashableKey(low, high)
	if memoizeKey in memoization:
		return memoization[memoizeKey]

	if low < 0 and high < 0:
		return False

	canMeasure = False
	for cup in measuringCups:
		cupLow, cupHigh = cup
		if low <= cupLow and cupHigh <= high:
			canMeasure = True
			break

		canMeasure = canMeasureInRange(measuringCups, low-cupLow, high-cupHigh, memoization)
		if canMeasure:
			break
	memoization[memoizeKey] = canMeasure
	return canMeasure

def createHashableKey(low, high):
	return str(low) + ":" + str(high)

print(AmbiguousMeasurements([[200,210],[450,465],[900,950]],1900,2200))