# O(n) time | O(n) space
def RunLengthEncoding(string):
	currentRunLength = 1
	encodedStringChars = []
	for i in range(1,len(string)):
		currentCharacter = string[i]
		previousCharacter = string[i-1]

		if currentCharacter != previousCharacter or currentRunLength == 9:
			encodedStringChars.append(str(currentRunLength))
			encodedStringChars.append(previousCharacter)
			currentRunLength = 0

		currentRunLength += 1

	encodedStringChars.append(str(currentRunLength))
	encodedStringChars.append(string[len(string)-1])

	return "".join(encodedStringChars)


print(RunLengthEncoding("AAAAAAAAAAAABBCCCCDDEEEFEFEFEFEFEFEFGGGGEEFFF"))