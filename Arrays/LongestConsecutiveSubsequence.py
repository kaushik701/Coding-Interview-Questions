# Leetcode #128: https://youtu.be/P6RZZMu_maU?si=bLL5PWIl-njwpVXS
# O(n) time | O(n) space
def LongestConsecutiveSubsequence(array):
	if len(array) == 0: 
		return 0
	arraySet = set(array)
	longest = 0
	for i in array:
		if (i-1) not in arraySet:
			length = 0
			while (i + length) in arraySet:
				length += 1
			longest = max(length,longest)
	return longest

print(LongestConsecutiveSubsequence([1]))