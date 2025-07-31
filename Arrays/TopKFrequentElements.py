# LeetCode #347: https://youtu.be/YPTqKIgVk-k?si=PZ66aB0ptTPTGKRD
# O(n) time | O(n) space
def TopKFrequentElements(array,k):
	count = {}
	freq = [[] for i in range(len(array)+1)]
	for n in array:
		count[n] = + count.get(n,0)
	for n, c in count.items():
		freq[c].append(n)
	res = []
	for i in range(len(freq)-1,0,-1):
		for n in freq[i]:
			res.append(n)
			if len(res) == k:
				return res

print(TopKFrequentElements([1,1,5,8,9,6,6,3,12,10],2))