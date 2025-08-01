# O(n^3) time | O(n) space
def LongestBalanceSubstring(string):
	maxLength = 0
	for i in range(len(string)):
		for j in range(i+2,len(string)+1,2):
			if isBalanced(string[i:j]):
				currentLength = j-i
				maxLength = max(maxLength,currentLength)

	return maxLength

def isBalanced(string):
	openParensStack = []

	for char in string:
		if char == "(":
			openParensStack.append("(")
		elif len(openParensStack) > 0:
			openParensStack.pop()
		else:
			return False

	return len(openParensStack) == 0

# O(n) time | O(n) space
def LongestBalanceSubstring1(string):
	maxLength = 0
	idxStack =[]
	idxStack.append(-1)

	for i in range(len(string)):
		if string[i] == "(":
			idxStack.append(i)
		else:
			idxStack.pop()
			if len(idxStack) == 0:
				idxStack.append(i)
			else:
				balancedSubstringStartIdx = idxStack[len(idxStack)-1]
				currentLength = i - balancedSubstringStartIdx
				maxLength = max(maxLength,currentLength)
	return maxLength

# O(n) time | O(1) space
def LongestBalanceSubstring2(string):
	maxLength = 0
	openingCount = 0
	closingCount = 0
	for char in string:
		if char == "(":
			openingCount += 1
		else:
			closingCount += 1
		if openingCount == closingCount:
			maxLength = max(maxLength,closingCount*2)
		elif closingCount > openingCount:
			openingCount = 0
			closingCount = 0

	openingCount = 0
	closingCount = 0
	for i in reversed(range(len(string))):
		char = string[i]
		if char == "(":
			openingCount += 1
		else:
			closingCount += 1

		if openingCount == closingCount:
			maxLength = max(maxLength, closingCount*2)
		elif openingCount > closingCount:
			openingCount = 0
			closingCount = 0
	return maxLength


print(LongestBalanceSubstring("(()))("))
print(LongestBalanceSubstring1("(()))("))
print(LongestBalanceSubstring2("(()))("))