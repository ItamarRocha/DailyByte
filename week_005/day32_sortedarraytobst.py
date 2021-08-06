"""
Given an array of numbers sorted in ascending order, return a height-balanced binary search tree using every number from the array.
Note: height-balanced meaning that the level of any node’s two subtrees should not differ by more than one.

Ex: Given the following nums...

nums = [1, 2, 3] return a reference to the following tree...
       2
      /  \
     1    3
Ex: Given the following nums...

nums = [1, 2, 3, 4, 5, 6] return a reference to the following tree...
        3
       / \
      2   5
      \  / \
       1 4  6
"""

class BST():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_bst(arr):
    if len(arr) == 0:
        return None

    mid = len(arr)//2

    root = BST(arr[mid])

    root.left = construct_bst(arr[:mid])
    root.right = construct_bst(arr[mid+1:])

    return root

arr = [1,2,3]
root = construct_bst(arr)

print(root.value == 2)
print(root.right.value == 3)
print(root.left.value == 1)

arr = [1,2,3,4,5,6]
root = construct_bst(arr)

print(root.value == 4)
print(root.left.value == 2)
print(root.left.left.value == 1)
print(root.left.right.value == 3)
print(root.right.value == 6)
print(root.right.left.value == 5)