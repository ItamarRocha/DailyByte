"""
Given a binary tree, returns of all its levels in a bottom-up fashion (i.e. last level towards the root). Ex: Given the following tree…

        2
       / \
      1   2
return [[1, 2], [2]]
Ex: Given the following tree…

       7
      / \
    6    2
   / \ 
  3   3 
return [[3, 3], [6, 2], [7]]
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time O(n), considering that we are using a deque in our output, or even a list with reversal in the end (2n)
# Space O(n)
def bottomsup(root):
    queue = [(0, root)]
    output = []

    while queue:
        level, node = queue.pop(0)

        if not node:
            continue

        queue.append((level + 1, node.left))
        queue.append((level + 1, node.right))

        if len(output) - 1 < level:
            output.insert(0, [node.value])
        else:
            output[0].append(node.value)
    
    return output

root = Tree(2)
root.left = Tree(1)
root.right = Tree(2)

print(bottomsup(root))

root = Tree(7)
root.left = Tree(6)
root.right = Tree(2)
root.left.left = Tree(3)
root.left.right = Tree(3)

print(bottomsup(root))