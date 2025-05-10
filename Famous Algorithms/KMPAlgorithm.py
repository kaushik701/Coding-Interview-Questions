# O(N+M) time | O(M) space
string = input("Enter a String: ")
subString = input("Enter a Substring: ")
def KMPAlgorithm(string,subString):
	pattern = buildPattern(subString)
	return doesMatch(string,subString,pattern)

def buildPattern(subString):
	pattern = [-1 for i in subString]
	j = 0 
	i = 1
	while i < len(subString):
		if subString[i] == subString[j]:
			pattern[i] = j
			i += 1
			j += 1
		elif j>0:
			j = pattern[j-1] + 1
		else:
			i += 1
	return pattern

def doesMatch(string,subString,pattern):
	i,j = 0,0
	while i+len(subString) - j <= len(string):
		if string[i] == subString[j]:
			if j == len(subString) -1:
				return True
			i += 1
			j += 1
		elif j>0:
			j = pattern[j-1] + 1
		else: i += 1
	return False

print(KMPAlgorithm(string,subString))