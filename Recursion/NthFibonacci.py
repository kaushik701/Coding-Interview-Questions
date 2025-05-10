# O(2^n) time | O(n) space 
def getNthFibonacci(number):
	if number == 2:
		return 1
	elif number == 1:
		return 0
	else:
		return getNthFibonacci(number-1) + getNthFibonacci(number-2)

# O(n) time | O(n) space
def getNthFibonacci2(number,memoize={1:0,2:1}):
	if number in memoize:
		return memoize[number]
	else:
		memoize[number] = getNthFibonacci2(number-1,memoize) + getNthFibonacci2(number-2,memoize)
		return memoize[number]

# O(n) time | O(1) space
def getNthFibonacci3(number):
	lastTwo = [0,1]
	counter = 3
	while counter <= number:
		nextFib = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = nextFib
		counter += 1
	return lastTwo[1] if number > 1 else lastTwo[0]

print(getNthFibonacci(22))
print(getNthFibonacci2(5))
print(getNthFibonacci3(5))