"""
Given a binary tree return all the values you’d be able to see if you were standing on the left side of it with values ordered from top to bottom.

Ex: Given the following tree…

-->    4
      / \
-->  2   7
return [4, 2]
Ex: Given the following tree…

-->        7
         /  \
-->     4     9
       / \   / \
-->   1   4 8   9
                 \
-->               9
return [7, 4, 1, 9]
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Just do a breadth first search storing the first value that appears from every level

def visiblevalues(root):
    queue = [(0, root)]
    output = []

    while queue:
        level, node = queue.pop(0)

        if not node:
            continue

        if len(output) - 1 < level:
            output.append(node.value)
        
        queue.append((level + 1, node.left))
        queue.append((level + 1, node.right))
    
    return output

root = Tree(2)
root.left = Tree(4)
root.right = Tree(7)

print(visiblevalues(root))

root = Tree(7)
root.left = Tree(4)
root.left.left = Tree(1)
root.left.right = Tree(4)
root.right = Tree(9)
root.right.right = Tree(9)
root.right.left = Tree(8)
root.right.right.right = Tree(9)

print(visiblevalues(root))