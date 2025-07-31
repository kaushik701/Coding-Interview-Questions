# Leetcode #238: https://youtu.be/bNvIQI2wAjk?si=lnirURaKwQAwOuIl
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

# O(n^2) time | O(n) space
def ArrayOfProducts1(array):
	if len(array) < 2:
		return

	products = [1 for _ in range(len(array))]
	for i in range(len(array)):
		runningProduct = 1
		for j in range(len(array)):
			if i != j:
				runningProduct *= array[j]
		products[i] = runningProduct

	return products

# O(n) time | O(n) space
def ArrayOfProducts2(array):
	if len(array) < 2:
		return 

	products = [1 for _ in range(len(array))]
	leftProducts = [1 for _ in range(len(array))]
	rightProducts = [1 for _ in range(len(array))]
	
	leftRunningProduct = 1
	for i in range(len(array)):
		leftProducts[i] = leftRunningProduct
		leftRunningProduct *= array[i]

	rightRunningProduct = 1
	for i in reversed(range(len(array))):
		rightProducts[i] = rightRunningProduct
		rightRunningProduct *= array[i] 

	for i in range(len(array)):
		products[i] = leftProducts[i] * rightProducts[i]
	
	return products

# O(n) time | O(n) space
def ArrayOfProducts3(array):
	if len(array) < 2:
		return

	products = [1 for _ in range(len(array))]
	leftRunningProduct = 1
	for i in range(len(array)):
		products[i] = leftRunningProduct
		leftRunningProduct *= array[i]

	rightRunningProduct = 1
	for i in reversed(range(len(array))):
		products[i] *= rightRunningProduct
		rightRunningProduct *= array[i]

	return products 

print(ArrayOfProducts(array))
print(ArrayOfProducts1(array))