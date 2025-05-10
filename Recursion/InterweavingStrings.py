# O(2^(n+m)time | O(n+m) space
def getInterweavingStrings(one,two,three):
	if len(three) != len(one) + len(two):
		return False
	return areInterwoven(one,two,three,0,0)

def areInterwoven(one,two,three,i,j):
	k=i+j
	if k == len(three):
		return True

	if i < len(one) and one[i] ==  three[k]:
		if areInterwoven(one,two,three,i+1,j):
			return True

	if j < len(two) and two[j] == three[k]:
		return areInterwoven(one,two,three,i,j+1)

	return False

# O(nm) time | O(nm) space
def getInterweavingStrings2(one,two,three):
	if len(three) != len(one) + len(two):
		return False
	cache = [[None for j in range(len(two)+1)] for i in range(len(one)+1)]
	return areInterwoven2(one,two,three,0,0)

def areInterwoven2(one,two,three,i,j,cache):
	if cache[i][j] is not None:
		return cache[i][j]
	k=i+j
	if k == len(three):
		return True

	if i < len(one) and one[i] ==  three[k]:
		cache[i][j] = areInterwoven2(one,two,three,i+1,j,cache)
		if cache[i][j]:
			return True

	if j < len(two) and two[j] == three[k]:
		cache[i][j] = areInterwoven2(one,two,three,i,j+1,cache)
		return cache[i][j]

	return False

print(getInterweavingStrings('aaa','aaabcb','aaabcbaab'))