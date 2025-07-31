# Leetcode #242: https://youtu.be/9UtInBqnCgA?si=suTKAW6oUBg6KZ6T
# O(n+m) time | O(n) space
def ValidAnagrams(str1,str2):
	if len(str1) != len(str2):
		return -1
	countStr1 = {}
	countStr2 = {}
	for i in range(len(str1)):
		countStr1[str1[i]] = 1 + countStr1.get(str1[i],0)
		countStr2[str2[i]] = 1 + countStr2.get(str2[i],0)
	for c in countStr1:
		if countStr1[c] != countStr2.get(c,0):
			return False
	return True

# O(n) time | O(n) space
from collections import Counter
def ValidAnagrams1(str1,str2):
	return Counter(str1) == Counter(str2)

# O(nlog(n)) time | O(n) space
def ValidAnagrams2(str1,str2):
	return sorted(str1) == sorted(str2)

print(ValidAnagrams("danger","gardan"))