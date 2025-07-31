# LeetCode #4: https://youtu.be/q6IEA26hvXc?si=7sBqrBsILkceE1W0
# O(log(m+n)) time | O(m+n) space
def MedianOfTwoSortedArrays(array1,array2):
	total = len(array1) + len(array2)
	half = total // 2
	if len(array1) < len(array2):
		array1, array2 = array2, array1

	left, right = 0, len(array1) - 1
	while True:
		i = (left + right) // 2
		j = half - i - 2

		array1Left = array1[i] if i >= 0 else float("-inf")
		array1Right = array1[i+1] if (i+1) < len(array1) else float("inf")
		array2Left = array2[j] if j >= 0 else float("-inf")
		array2Right = array2[j+1] if (j+1) < len(array2) else float("inf")

		if array1Left <= array2Right and array2Left <= array1Right:
			if total % 2:
				return min(array1Right,array2Right)
			return (max(array1Left,array2Left) + min(array1Right,array2Right)) / 2
		elif array1Left > array2Right:
			right = i - 1
		else:
			left = i + 1

print(MedianOfTwoSortedArrays([1,3],[2,4]))