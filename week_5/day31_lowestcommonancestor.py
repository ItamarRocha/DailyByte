"""
Given a binary search tree that contains unique values and two nodes within the tree, a, and b, return their lowest common ancestor. 
Note: the lowest common ancestor of two nodes is the deepest node within the tree such that both nodes are descendants of it.

Ex: Given the following tree...
       7
      / \
    2    9
   / \ 
  1   5 
and a = 1, b = 9, return a reference to the node containing 7.
Ex: Given the following tree...

        8
       / \
      3   9
     / \ 
    2   6
and a = 2, b = 6, return a reference to the node containing 3.
Ex: Given the following tree...

        8
       / \
      6   9
and a = 6, b = 8, return a reference to the node containing 8.
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# first solution
class Answer():
    def __init__(self):
        self.ans = None

def lca_tree_recursor(root, a, b, ans):
    if not root:
        return 0
    
    left = lca_tree_recursor(root.left, a, b, ans)
    right = lca_tree_recursor(root.right, a, b, ans)

    mid = root.value == a or root.value == b

    if left + right + mid == 2:
        ans.ans = root
    
    return mid or left or right

def lowestCommonAncestor(root, a, b):
    ans = Answer()
    lca_tree_recursor(root, a, b, ans)
    return ans.ans

root = Tree(7)
root.left = Tree(2)
root.right = Tree(9)
root.left.left = Tree(1)
root.left.right = Tree(5)

print(lowestCommonAncestor(root, 1, 9).value) # 7

root = Tree(8)
root.left = Tree(3)
root.right = Tree(9)
root.left.left = Tree(2)
root.left.right = Tree(6)

print(lowestCommonAncestor(root, 2, 6).value) # 3

root = Tree(8)
root.left = Tree(6)
root.right = Tree(9)

print(lowestCommonAncestor(root, 6, 8).value) # 8