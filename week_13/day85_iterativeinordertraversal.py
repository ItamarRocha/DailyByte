"""
Given a binary tree, return a list containing its inorder traversal without using recursion.

Ex: Given the following tree…

      2     
     / \   
    1   3
return [1, 2, 3]
Ex: Given the following tree…

        2
       / \
      1   7
     / \
    4   8
return [4, 1, 8, 2, 7]
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.seen = False

# def iterative_inorder_traversal(root):
#     output = []

#     stack = [root]

#     while stack:
#         if stack[-1].left and not stack[-1].left.seen: # works with modification in the tree class
#             stack.append(stack[-1].left)
#             continue
#         el = stack.pop()
#         el.seen = True
#         output.append(el.value)
#         if el.right:
#             stack.append(el.right)

#     return output

def iterative_inorder_traversal(root):
    output = []
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return output
        node = stack.pop()
        output.append(node.value)
        root = node.right

root = Tree(2)
root.left = Tree(1)
root.right = Tree(3)

print(iterative_inorder_traversal(root))

root = Tree(2)
root.left = Tree(1)
root.right = Tree(7)
root.left.left = Tree(4)
root.left.right = Tree(8)

print(iterative_inorder_traversal(root))
