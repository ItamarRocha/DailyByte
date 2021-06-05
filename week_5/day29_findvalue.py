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

# Time O(n)
# Space O(n) | can be O(h) if balanced tree
def find_value(root, value):
    if root == None:
        return None
    
    if value > root.value:
        return find_value(root.right)
    elif value < root.value:
        return find_value(root.left)
    
    return value

