"""
Given a binary tree, return the largest value in each of its levels. Ex: Given the following tree…

    2
   / \
  10  15
        \
         20
return [2, 15, 20]
Ex: Given the following tree…

          1
         / \
        5   6
       / \   \  
      5   3   7 
return [1, 6, 7]
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time O(n)
# Space O(n)
def max_value_in_each_level(root):
    queue = [(0, root)]
    output = []

    while queue:
        level, node = queue.pop(0)

        if not node:
            continue

        queue.append((level + 1, node.left))
        queue.append((level + 1, node.right))

        if len(output) - 1 < level:
            output.append(node.value)
        else:
            output[level] = max(output[level], node.value)
        
    return output

root = Tree(2)
root.left = Tree(10)
root.right = Tree(15)
root.right.right = Tree(20)

print(max_value_in_each_level(root))

root = Tree(1)
root.left = Tree(5)
root.left.left = Tree(5)
root.left.right = Tree(3)
root.right = Tree(6)
root.right.right = Tree(7)

print(max_value_in_each_level(root))