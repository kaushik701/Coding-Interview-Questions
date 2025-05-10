# O(n) time | O(d) space
def ProductSum(array,multiplier=1):
	Sum = 0
	for element in array:
		if type(element) is list:
			Sum += ProductSum(element,multiplier+1)
		else:
			Sum += element
	return Sum * multiplier

print(ProductSum([1,8,7,[5,6,9],4,2,3,[2],5,6,10,[22,56],3]))
print(ProductSum([1,8,7,[5,6,9],4,2,3,2]))
print(ProductSum([1,8,7,[5,6,9],4,2,3,[2]]))
print(ProductSum([1,8,7,[5,6,9],4,2,3,[2],[20,50,[25,1]],4]))
print(ProductSum([2,7,5,3,[29,33,520,1],22,52]))
print(ProductSum([3,5,9,22,33,39,[33,62,75,[75,76,77]]]))
print(ProductSum([2,5,25,30,[33,31,45,49],77,81]))