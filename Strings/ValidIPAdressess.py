# O(1) time | O(1) space
def ValidIPAdressess(string):
	if len(string) == 0: 
		return "IP Not Found"
	ipAdressessFound = []
	for i in range(1,min(len(string),4)):
		currentIPAdressParts = ['','','','']
		currentIPAdressParts[0] = string[:i]
		if not isValidPart(currentIPAdressParts[0]):
			continue
		
		for j in range(i+1,i+min(len(string)-i,4)):
			currentIPAdressParts[1] = string[i:j]
			if not isValidPart(currentIPAdressParts[1]):
				continue

			for k in range(j+1, j+min(len(string)-j,4)):
				currentIPAdressParts[2] = string[j:k]
				currentIPAdressParts[3] = string[k:]
				if isValidPart(currentIPAdressParts[2]) and isValidPart(currentIPAdressParts[3]):
					ipAdressessFound.append('.'.join(currentIPAdressParts))
	return ipAdressessFound

def isValidPart(string):
	stringAsInt = int(string)
	if stringAsInt > 255:
		return False
	return len(string) == len(str(stringAsInt))

print(ValidIPAdressess("192809879"))