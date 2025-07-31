# O(m*(n+m)) time | O(1) space
def GenerateDocument(characters, document):
	for character in document:
		documentFrequency = countCharacterFrequency(character, document)
		charactersFrequency = countCharacterFrequency(character,characters)
		if documentFrequency > charactersFrequency: 
			return False
	return True

def countCharacterFrequency(character,target):
	frequency = 0
	for char in target:
		if char == character:
			frequency += 1
	return frequency


# O(c*(n+m)) time | O(c) space
def GenerateDocument1(characters,document):
	alreadyCounted = set()
	for character in document:
		if character in alreadyCounted:
			continue

	documentFrequency = countCharacterFrequency(character, document)
		charactersFrequency = countCharacterFrequency(character,characters)
		if documentFrequency > charactersFrequency: 
			return False
		alreadyCounted.add(character)
	return True

# O(n+m) time | O(c) space
def GenerateDocument2(characters,document):
	characterCounts = {}
	for character in characters:
		if character not in characterCounts:
			characterCounts[character] = 0
		characterCounts[character] += 1

	for character in document:
		if character not in characterCounts or characterCounts[character] == 0:
			return False
		characterCounts[character] -= 1
	return True