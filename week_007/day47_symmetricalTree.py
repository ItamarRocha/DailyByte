"""
Given a binary tree, return whether or not it forms a reflection across its center (i.e. a line drawn straight down starting from the root).
Note: a reflection is when an image, flipped across a specified line, forms the same image.

Ex: Given the following tree…

   2
 /   \
1     1
return true as when the tree is reflected across its center all the nodes match.
Ex: Given the following tree…

    1
   / \
  5   5
   \    \
    7    7
return false as when the tree is reflected across its center the nodes containing sevens do not match.
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time O(n)
# Space O(2n)
def bfs(root, left=True):
    output = []
    queue = [(0,0,root)]
    while queue:
        depth, horiz, node = queue.pop(0)

        if not node:
            continue

        if left:
            queue.append((depth + 1, horiz + 1, node.left))
            queue.append((depth + 1, horiz - 1, node.right))
        else:
            queue.append((depth + 1, horiz + 1, node.right))
            queue.append((depth + 1, horiz - 1, node.left))


        output.append((depth, horiz, node.value))
    
    return output

def symmetricaltree(root):
    output1 = bfs(root.left, left=True)
    output2 = bfs(root.right, left=False)

    print(output1 == output2)

root = Tree(2)
root.left = Tree(1)
root.right = Tree(1)

symmetricaltree(root)

root = Tree(1)
root.left = Tree(5)
root.right = Tree(5)
root.left.right = Tree(7)
root.right.right = Tree(7)

symmetricaltree(root)

root = Tree(1)
root.left = Tree(2)
root.right = Tree(2)
root.left.right = Tree(4)
root.left.left = Tree(3)
root.right.left = Tree(4)
root.right.right = Tree(3)

symmetricaltree(root)

# time O(n)
# Space O(n)
def symmetricaltree(root):
    if not root:
        return True
    stack = [(root.left, root.right)]
    while stack:
        l, r = stack.pop()
        if not l and not r:
            continue
        if not l or not r or (l.value != r.value):
            return False
        stack.append((l.left, r.right))
        stack.append((l.right, r.left))
    return True

print("solution 2:\n")
root = Tree(2)
root.left = Tree(1)
root.right = Tree(1)

print(symmetricaltree(root))

root = Tree(1)
root.left = Tree(5)
root.right = Tree(5)
root.left.right = Tree(7)
root.right.right = Tree(7)

print(symmetricaltree(root))

root = Tree(1)
root.left = Tree(2)
root.right = Tree(2)
root.left.right = Tree(4)
root.left.left = Tree(3)
root.right.left = Tree(4)
root.right.right = Tree(3)

print(symmetricaltree(root))