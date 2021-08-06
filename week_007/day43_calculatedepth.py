"""
Given a binary tree, return its maximum depth.
Note: the maximum depth is defined as the number of nodes along the longest path from root node to leaf node.

Ex: Given the following tree…

    9
   / \
  1   2
return 2
Ex: Given the following tree…

    5
   / \
  1  29
    /  \
   4   13
return 3
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time O(n)
# Space O(d) d -> max possible depth 
def calculatedepth(root):
    if not root:
        return 0

    max_depth = max(calculatedepth(root.left), calculatedepth(root.right)) + 1
    
    return max_depth

root = Tree(9)
root.left = Tree(1)
root.right = Tree(2)

print(calculatedepth(root))

root = Tree(5)
root.left = Tree(1)
root.right = Tree(29)
root.right.left = Tree(4)
root.right.right = Tree(13)

print(calculatedepth(root))