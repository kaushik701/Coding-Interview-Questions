# Leetcode #567: https://youtu.be/UbyhOgBN834?si=0F0GpJfCq8GdftKw
# O(n) time | O(n) space
def StringPermutation(str1,str2):
	if len(str1) > len(str2):
		return False
	str1Count, str2Count = [0]*26,[0]*26
	for i in range(len(str1)):
		str1Count[ord(str1[i])-ord('a')] += 1
		str2Count[ord(str2[i])-ord('a')] += 1

	matches = 0
	for i in range(26):
		if str1Count[i] == str2Count[i]:
			matches += 1
		else 0

	l = 0
	for r in range(len(str1),len(str2)):
		if matches == 26: return True

		index = ord(str2[r]) - ord('a')
		str2Count[index] += 1
		if str1Count[index] == str2Count[index]:
			matches += 1
		elif str1Count[index] + 1 == str2Count[index]:
			matches -= 1

		index = ord(str2[l]) - ord('a')
		str2Count[index] -= 1
		if str1Count[index] == str2Count[index]:
			matches += 1
		elif str1Count[index] + 1 == str2Count[index]:
			matches -= 1
	return matches == 26
