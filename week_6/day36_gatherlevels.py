"""
Given a binary tree, return its level order traversal where the nodes in each level are ordered from left to right.

Ex: Given the following tree...

    4
   / \
  2   7
return [[4], [2, 7]]
Ex: Given the following tree...

    2
   / \
  10  15
        \
         20
return [[2], [10, 15], [20]]
Ex: Given the following tree...

    1
   / \
  9   32
 /      \
3        78
return [[1], [9, 32], [3, 78]]
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time O(n)
# Space O(n)
def gather_levels(root):
    output = []
    queue = []

    queue.append((0, root))

    while queue:

        level, node = queue.pop(0)

        if not node:
            continue

        queue.append((level + 1, node.left))
        queue.append((level + 1, node.right))

        if len(output) - 1 < level:
            output.append([node.value])
        else:
            output[level].append(node.value)
    
    return output

root = Tree(4)
root.left = Tree(2)
root.right = Tree(7)

print(gather_levels(root))

root = Tree(2)
root.left = Tree(10)
root.right = Tree(15)
root.right.right = Tree(20)

print(gather_levels(root))

root = Tree(1)
root.left = Tree(9)
root.left.left = Tree(3)
root.right = Tree(32)
root.right.right = Tree(78)

print(gather_levels(root))

root = Tree(1)
root.left = Tree(9)
root.left.left = Tree(3)
root.left.right = Tree(2)
root.right = Tree(32)
root.right.left = Tree(40)
root.right.right = Tree(78)

print(gather_levels(root))