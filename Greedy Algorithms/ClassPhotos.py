# O(nlog(n)) time | O(1) space
def ClassPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)

	shirtColorInFirstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
	for idx in range(len(redShirtHeights)):
		redShirtHeight = redShirtHeights[idx]
		blueShirtHeight = blueShirtHeights[idx]

		if shirtColorInFirstRow == "RED":
			if redShirtHeight >= blueShirtHeight:
				return False
		else:
			if blueShirtHeight >= redShirtHeight:
				return False
	return True

print(ClassPhotos([5,8,1,3,4],[6,9,2,4,5]))