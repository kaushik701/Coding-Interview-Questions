# O(n^2) time | O(n) space
array = list(map(int,input('Enter the Numbers: ').split()))
def ArrayOfProducts(array):
	if len(array) < 2:
		return []
	productArray = [0] * len(array)
	product = 1
	for i in range(len(array)):
		productArray[i] = product
		product *= array[i]
	product = 1
	for i in reversed(range(len(array))):
		productArray[i] *= product
		product *= array[i]
	return productArray
print(ArrayOfProducts(array))