# O(nlog(n)) time | O(1) space
def TandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()

	if not fastest:
		reverseArrayInPlace(redShirtSpeeds)

	totalSpeed = 0
	for idx in range(len(redShirtSpeeds)):
		rider1 = redShirtSpeeds[idx]
		rider2 = blueShirtSpeeds[len(blueShirtSpeeds)-idx-1]
		totalSpeed += max(rider1,rider2)
	return totalSpeed

def reverseArrayInPlace(array):
	start = 0
	end = len(array) - 1
	while start < end:
		array[start], array[end] = array[end], array[start]
		start += 1
		end -= 1

print(TandemBicycle([5,5,3,9,2],[3,6,7,2,1,8],True))