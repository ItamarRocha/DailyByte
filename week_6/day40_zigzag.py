"""
Given a binary tree, return its zig-zag level order traversal (i.e. its level order traversal from left to right the first level, right to left the level the second, etc.).

Ex: Given the following tree…

    1
   / \
  2   3
return [[1], [3, 2]]
Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return [[8], [29, 2], [3, 9]]
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time O(n²) # cause we are reversing a list inside a loop
# Space O(2^m * log)
def zigzag_traversal(root):
    queue = [(0,root)]

    output = []

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

    reverse = False
    for i in range(len(output)):
        if i % 2 != 0:
            output[i] = output[i][::-1]
    
    return output


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)

print(zigzag_traversal(root))

root = Tree(8)
root.left = Tree(2)
root.right = Tree(29)
root.right.left = Tree(3)
root.right.right = Tree(9)

print(zigzag_traversal(root))