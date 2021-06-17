"""
Given a binary tree, return its column order traversal from top to bottom and left to right. Note: if two nodes are in the same row and column, order them from left to right.

Ex: Given the following tree…

    8
   / \
  2   29
     /  \
    3    9
return [[2], [8, 3], [29], [9]]
Ex: Given the following tree…

     100
    /   \
  53     78
 / \    /  \
32  3  9    20
return [[32], [53], [100, 3, 9], [78], [20]]
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def gather_columns(root):
    queue = [(0, root)]
    output = {}

    while queue:
        column, node = queue.pop(0)

        if not node:
            continue
        
        if column not in output:
            output[column] = [node.value]
        else:
            output[column].append(node.value)

        queue.append((column - 1, node.left))
        queue.append((column + 1, node.right))        
    
    sorted_keys = [x for x in output.keys()]
    sorted_keys.sort()
    
    output = [output[key] for key in sorted_keys]

    return output

root = Tree(8)
root.left = Tree(2)
root.right = Tree(29)
root.right.left = Tree(3)
root.right.right = Tree(9)

print(gather_columns(root))

root = Tree(100)
root.left = Tree(53)
root.left.left = Tree(32)
root.left.right = Tree(3)
root.right = Tree(78)
root.right.left = Tree(9)
root.right.right = Tree(20)

print(gather_columns(root))