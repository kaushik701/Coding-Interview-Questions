# O(n^2) time | O(n) space
string = input('Enter the String: ')
def PalindromeCheck(string):
	reversedString = ""
	for i in reversed(range(len(string))):
		reversedString += string[i]
	return string ==  reversedString
# O(n) time | O(n) space
def PalindromeCheck1(string):
	reversedChars = []
	for i in reversed(range(len(string))):
		reversedChars.append(string[i])
	return string == "".join(reversedChars)

# O(n) time | O(n) space
def PalindromeCheck2(string,i=0):
	j = len(string)-1-i
	return True if i >= j else string[i] == string[j] and PalindromeCheck2(string,i+1)

# O(n) time | O(1) space
def PalindromeCheck3(string):
	leftIdx = 0
	rightIdx = len(string)-1
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]:
			return False
		leftIdx += 1
		rightIdx -= 1
	return True

print(PalindromeCheck(string))
print(PalindromeCheck1(string))
print(PalindromeCheck2(string))
print(PalindromeCheck3(string))