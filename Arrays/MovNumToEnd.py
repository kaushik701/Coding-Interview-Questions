# O(n) time | O(1) space
array = list(map(int,input('Enter the nos: ').split()))
toMove = int(input('Enter the no.: '))
def movNumtoEnd(array,toMove):
	i = 0
	j = len(array)-1
	while i < j:
		while i < j and array[j] == toMove:
			j -= 1
		if array[i] == toMove:
			array[i],array[j] = array[j],array[i]
		i += 1
	return array

print(movNumtoEnd(array,toMove))