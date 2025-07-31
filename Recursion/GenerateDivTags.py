# O((2n)!/n!*((n+1)!)) time | O((2n)!/n!*((n+1)!)) space
def GenerateDivTags(numberOfTags):
	matchedDivTags = []
	GenerateDivTagsFromPrefix(numberOfTags, numberOfTags, "",matchedDivTags)
	return matchedDivTags

def GenerateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded, prefix, result):
	if openingTagsNeeded > 0:
		newPrefix = prefix + "<div>"
		GenerateDivTagsFromPrefix(openingTagsNeeded-1, closingTagsNeeded, newPrefix, result)

	if openingTagsNeeded < closingTagsNeeded:
		newPrefix = prefix + "</div>"
		GenerateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded-1, newPrefix, result)

	if closingTagsNeeded == 0:
		result.append(prefix) 

print(GenerateDivTags(4))