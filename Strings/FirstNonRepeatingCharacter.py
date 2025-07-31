# O(n^2) time | O(1) space
def FirstNonRepeatingCharacter(string):
	for idx1 in range(len(string)):
		foundDuplicate = False
		for idx2 in range(len(string)):
			if string[idx1] == string[idx2] and idx1 != idx2:
				foundDuplicate = True

		if not foundDuplicate:
			return idx1
	return -1

# O(n) time | O(1) space
def FirstNonRepeatingCharacter1(string):
	characterFrequencies = {}
	for character in string:
		characterFrequencies[character] = characterFrequencies.get(character,0) + 1
	for idx in range(len(string)):
		character = string[idx]
		if characterFrequencies[character] == 1:
			return idx
	return -1

print(FirstNonRepeatingCharacter("kaushil"))
print(FirstNonRepeatingCharacter1("kaushik"))