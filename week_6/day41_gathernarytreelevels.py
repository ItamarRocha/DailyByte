"""
The Daily Byte
Good morning,

Today's Byte

Given an n-ary tree, return its level order traversal.
Note: an n-ary tree is a tree in which each node has no more than N children.

Ex: Give the following n-ary tree…

    8
  / | \
 2  3  29
return [[8], [2, 3, 29]]
Ex: Given the following n-ary tree…

     2
   / | \
  1  6  9
 /   |   \
8    2    2
   / | \
 19 12 90
return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]
"""
class NaryTree():
    def __init__(self, value):
        self.value = value
        self.children = []

def gather_levels(root):
    output = []
    queue = []

    queue.append((0, root))

    while queue:

        level, node = queue.pop(0)

        if not node:
            continue

        for child in node.children:
            queue.append((level + 1, child))

        if len(output) - 1 < level:
            output.append([node.value])
        else:
            output[level].append(node.value)
    
    return output

root = NaryTree(8)
root.children.append(NaryTree(2))
root.children.append(NaryTree(3))
root.children.append(NaryTree(29))

print(gather_levels(root))

root = NaryTree(2)
root.children.append(NaryTree(1))
root.children[0].children.append(NaryTree(8))
root.children.append(NaryTree(6))
root.children[1].children.append(NaryTree(2))
root.children[1].children[0].children.append(NaryTree(19))
root.children[1].children[0].children.append(NaryTree(12))
root.children[1].children[0].children.append(NaryTree(90))
root.children.append(NaryTree(9))
root.children[2].children.append(NaryTree(2))

print(gather_levels(root))