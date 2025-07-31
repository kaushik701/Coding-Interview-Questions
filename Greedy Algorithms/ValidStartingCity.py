# O(n^2) time | O(1) space
def ValidStartingCity(distances,fuel,mpg):
	numberOfCities = len(distances)
	for startCityIdx in range(numberOfCities):
		milesRemaining = 0

		for currentCityIdx in range(startCityIdx, startCityIdx+numberOfCities):
			if milesRemaining < 0:
				continue
			currentCityIdx = currentCityIdx % numberOfCities
			fuelFromCurrentCity = fuel[currentCityIdx]
			distanceToNextCity = distances[currentCityIdx]
			milesRemaining += fuelFromCurrentCity * mpg - distanceToNextCity

		if milesRemaining >= 0:
			return startCityIdx
	return -1

# O(n) time | O(1) space
def ValidStartingCity1(distances, fuel, mpg):
	numberOfCities  = len(distances)
	milesRemaining = 0

	indexOfStartCityCandidate = 0
	milesRemainingAtStartingCityCandidate = 0

	for cityIdx in range(1, numberOfCities):
		distanceFromPreviousCity = distances[cityIdx-1]
		fuelFromPreviousCity = fuel[cityIdx-1]
		milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity

		if milesRemaining < milesRemainingAtStartingCityCandidate:
			milesRemainingAtStartingCityCandidate = milesRemaining
			indexOfStartCityCandidate = cityIdx
	return indexOfStartCityCandidate

print(ValidStartingCity([5,25,10,15,20],[1,2,1,0,3],10))
print(ValidStartingCity1([5,25,10,15,20],[1,2,1,0,3],10))