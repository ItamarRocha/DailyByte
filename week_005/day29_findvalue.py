"""
This question is asked by Google. Given the reference to the root of a binary search tree and a search value, return the reference to the node that contains the value if it exists and null otherwise.
Note: all values in the binary search tree will be unique.

Ex: Given the tree...

        3
       / \
      1   4
and the search value 1 return a reference to the node containing 1.
Ex: Given the tree

        7
       / \
      5   9
         / \ 
        8   10
and the search value 9 return a reference to the node containing 9.
Ex: Given the tree

        8
       / \
      6   9
and the search value 7 return null.
"""

class BST():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# Time O(n) | can be O(log n) if balanced
# Space O(n) | can be O(h) if balanced 
def find_value(root, value):
    if root == None:
        return None
    
    if value > root.value:
        return find_value(root.right, value)
    elif value < root.value:
        return find_value(root.left, value)
    
    return root

#     3
#    / \
#   1   4

bst = BST(3)
bst.left = BST(1)
bst.right = BST(4)

print(find_value(bst, 1).value)

#     7
#    / \
#   5   9
#      / \ 
#     8   10

bst = BST(7)
bst.left = BST(5)
bst.right = BST(9)
bst.right.left = BST(8)
bst.right.right = BST(10)

print(find_value(bst, 9).value)

#     8
#    / \
#   6   9

bst = BST(8)
bst.left = BST(6)
bst.right = BST(9)

print(find_value(bst, 7))