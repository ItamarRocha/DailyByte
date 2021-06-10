"""
Given a binary search tree, return its mode (you may assume the answer is unique). If the tree is empty, return -1. Note: the mode is the most frequently occurring value in the tree.

Ex: Given the following tree...

        2
       / \
      1   2
return 2.

Ex: Given the following tree...

         7
        / \
      4     9
     / \   / \
    1   4 8   9
               \
                9  
return 9.
"""
class BST():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# Solution 1
# Time O(n) n -> number of nodes
# Space O(m) m -> the number of different values'
def findmode(root):
    if not root:
        return -1

    els = {}

    dfs(root,els)

    mode = None
    cur_max = float("-inf")

    for key in els.keys():
        if els[key] > cur_max:
            cur_max = els[key]
            mode = key

    return mode

def dfs(root, els):
    if not root:
        return
    
    dfs(root.left, els)

    if root.value not in els:
        els[root.value] = 1
    else:
        els[root.value] += 1

    dfs(root.right, els)

    return

root = BST(2)
root.left = BST(1)
root.right = BST(2)

print(findmode(root))

root = BST(7)
root.left = BST(4)
root.left.left = BST(1)
root.left.right = BST(4)
root.right = BST(9)
root.right.left = BST(8)
root.right.right = BST(9)
root.right.right.right = BST(9)

print(findmode(root))

print("\n\nSolution2:\n")
# Solution 2
# Time O(n) n -> number of nodes
# Space O(1)
def findmode(root):
    if not root:
        return -1

    els = {"current_count" : float("-inf"),
            "current_el" : None,
            "max_count" : float("-inf"),
            "max_el" : None}

    dfs(root,els)

    return els["max_el"]

def dfs(root, els):
    if not root:
        return
    
    dfs(root.left, els)

    if root.value == els["current_el"]:
        els["current_count"] += 1
    else:
        els["current_el"] = root.value
        els["current_count"] = 1
    
    if els["current_count"] > els["max_count"]:
        els["max_count"] = els["current_count"]
        els["max_el"] = els["current_el"]

    dfs(root.right, els)

    return

root = BST(2)
root.left = BST(1)
root.right = BST(2)

print(findmode(root))

root = BST(7)
root.left = BST(4)
root.left.left = BST(1)
root.left.right = BST(4)
root.right = BST(9)
root.right.left = BST(8)
root.right.right = BST(9)
root.right.right.right = BST(9)

print(findmode(root))