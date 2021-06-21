"""
Given a binary tree, containing unique values, determine if it is a valid binary search tree.
Note: the invariants of a binary search tree (in our case) are all values to the left of a given node are less than the current node’s value, all values to the right of a given node are greater than the current node’s value, and both the left and right subtrees of a given node must also be binary search trees.

Ex: Given the following binary tree…

   1
 /   \
2     3
return false.
Ex: Given the following tree…

   2
 /   \
1     3
return true.
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time O(n)
# Space O(h or n) (call stack)
def validatetree(root, lb=float("-inf"), ub=float("inf")):
    if not root: return True

    if lb < root.value < ub and validatetree(root.left, lb, root.value) and \
        validatetree(root.right, root.value, ub):
        return True
    
    return False

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)

print(validatetree(root))

root = Tree(2)
root.left = Tree(1)
root.right = Tree(3)

print(validatetree(root))