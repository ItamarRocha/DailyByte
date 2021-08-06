"""
This question is asked by Google. Given an array of integers, return whether or not two numbers sum to a given target, k.
Note: you may not sum a number with itself.

Ex: Given the following...

    [1, 3, 8, 2], k = 10, return true (8 + 2)
    [3, 9, 13, 7], k = 8, return false
    [4, 2, 6, 5, 2], k = 4, return true (2 + 2)
"""

# Time O(n) Space O(n)
def twoNumberSum(array, targetSum):
    complement = set()

    for el in array:
        if el in complement:
            return True
        else:
            complement.add(targetSum-el)
    
    return False

print(twoNumberSum([1,3,8,2], 10))
print(twoNumberSum([3,9,13,7], 8))
print(twoNumberSum([4,2,6,5,2], 4))

# Time O(nlogn) Space O(1)
def twoNumberSum(array, targetSum):
	array.sort()
	
	left = 0
	right = len(array) - 1
	
	while left <= right:
		currentsum = array[left] + array[right]
		
		if currentsum < targetSum:
			left += 1
		elif currentsum > targetSum:
			right -= 1
		else:
			return True
	
	return False

print(twoNumberSum([1,3,8,2], 10))
print(twoNumberSum([3,9,13,7], 8))
print(twoNumberSum([4,2,6,5,2], 4))