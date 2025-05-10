 # https://youtu.be/dXV83KXt7KA?si=uvX1eoCKlJXLq7fP

 # O(n) time | O(1) space

 def KthLargestElement(array,k):
 	k = len(array)-k
 	return quickSelect(0,len(array)-1)

 def quickSelect(l,r):
 	less, equal, greater, pivot = l,l,r,array[r]
 	while equal <= greater:
 		while equal <= greater and array[equal] < pivot:
 			array[equal], array[less] = array[less],array[equal]
 			less += 1
 			equal += 1
 		while equal <= greater and array[equal] == pivot:
 			equal += 1
 		while equal <= greater and array[equal] > pivot:
 			array[equal], array[greater] = array[greater], array[equal]
 			greater -= 1

 	if k > greater:
 		return quickSelect(greater+1,r)
 	elif k < less:
 		return quickSelect(l,less-1)
 	else:
 		return array[greater]