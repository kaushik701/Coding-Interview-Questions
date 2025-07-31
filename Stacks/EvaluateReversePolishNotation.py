# Leetcode #150: https://youtu.be/iu0082c4HDE?si=gPUuhNIstIPv4_7g
# O(n) time | O(n) space
def EvaluateReversePolishNotation(tokens):
	stack = []
	for c in tokens:
		if c == "+":
			stack.append(stack.pop() + stack.pop())
		elif c == "-":
			a,b = stack.pop() , stack.pop()
			stack.append(b-a)
		elif c == "*":
			stack.append(stack.pop() * stack.pop())
		elif c == "/":
			a,b = stack.pop() , stack.pop()
			stack.append(int(b/a))
		else:
			stack.append(int(c))
	return stack[0]

print(EvaluateReversePolishNotation(["2","1","-","4","*","12","/"]))