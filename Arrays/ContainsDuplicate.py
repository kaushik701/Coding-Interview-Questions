# LeetCode #217 - https://youtu.be/3OamzN90kPg?si=lp45JSZRTXxR-9x9
# O(n) time | O(n) space
def ContainsDuplicate(array):
	duplicates = set()
	for i in array:
		if i in duplicates:
			return True
		duplicates.add(i)
	return False

print(ContainsDuplicate([1,4,5,2,3]))