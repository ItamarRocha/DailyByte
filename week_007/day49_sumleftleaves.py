"""
Given a binary tree, return the sum of all left leaves of the tree. Ex: Given the following tree…

    5
   / \
  2   12
     /  \
    3    8
return 5 (i.e. 2 + 3)
Ex: Given the following tree…

       2
      / \
    4    2
   / \ 
  3   9 
return 3
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Time O(n)
# Space O(n)
def sumleftleaves(root, isleft=False):
    if not root:
        return 0

    left = sumleftleaves(root.left, isleft=True)
    right = sumleftleaves(root.right, isleft=False)

    return left + right + (root.value if isleft and not root.left and not root.right else 0)

root = Tree(5)
root.left = Tree(2)
root.right = Tree(12)
root.right.left = Tree(3)
root.right.right = Tree(8)

print(sumleftleaves(root))

root = Tree(2)
root.left = Tree(4)
root.right = Tree(2)
root.left.left = Tree(3)
root.left.right = Tree(9)

print(sumleftleaves(root))

# Time O(n)
# Space O(n)
print("Solution 2:\n")
def sumleftleaves(root):
    queue = [(root, False)]
    total = 0
    while queue:
        node, isleft = queue.pop(0)

        if not node:
            continue
        
        queue.append((node.left, True))
        queue.append((node.right, False))

        if isleft and not node.left and not node.right:
            total += node.value
    return total

root = Tree(5)
root.left = Tree(2)
root.right = Tree(12)
root.right.left = Tree(3)
root.right.right = Tree(8)

print(sumleftleaves(root))

root = Tree(2)
root.left = Tree(4)
root.right = Tree(2)
root.left.left = Tree(3)
root.left.right = Tree(9)

print(sumleftleaves(root))