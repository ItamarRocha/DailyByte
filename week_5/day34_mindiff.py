"""
Given a binary search tree, return the minimum difference between any two nodes in the tree.

Ex: Given the following tree...
        2
       / \
      3   1
return 1.
Ex: Given the following tree...
        29
       /  \
     17   50
    /     / \
   1    42  59
return 8.
Ex: Given the following tree...
        2
         \
         100
return 98.
"""
class BST():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# Solution 1
# Time O(n)
# Space O(n)
def min_diff(root):
    output = []
    dfs(root, output)

    min_diff = float("inf")
    
    for i in range(1,len(output)):
        min_diff = min(min_diff, output[i] - output[i - 1])
    print(output)
    return min_diff

def dfs(root, output):
    if not root:
        return

    dfs(root.left, output)

    output.append(root.value)

    dfs(root.right, output)

    return

root = BST(2)
root.left = BST(1)
root.right = BST(3)

print(min_diff(root))

root = BST(29)
root.left = BST(17)
root.left.left = BST(1)
root.right = BST(50)
root.right.left = BST(42)
root.right.right = BST(59)

print(min_diff(root))

root = BST(2)
root.right = BST(100)

print(min_diff(root))

print("\n\nSolution 2:\n")

# Solution 2
# Time O(n)
# Space avg O(logn) worst O(n) #call stack
def min_diff(root):
    return dfs(root, float('-inf'), float('inf'))

def dfs(node, lo, hi):
    if not node: return hi - lo
    left = dfs(node.left, lo, node.value)
    right = dfs(node.right, node.value, hi)
    
    return min(left, right)
        

root = BST(2)
root.left = BST(1)
root.right = BST(3)

print(min_diff(root))

root = BST(29)
root.left = BST(17)
root.left.left = BST(1)
root.right = BST(50)
root.right.left = BST(42)
root.right.right = BST(59)

print(min_diff(root))

root = BST(2)
root.right = BST(100)

print(min_diff(root))


class Solution:
    Inf = float('inf')
    def getMinimumDifference(self, root): # -> int:
        self.best = Inf = self.Inf
        def dfs(n,a,b):
            if n:
                x = n.val
                self.best = min( self.best, x-a, b-x )
                dfs(n.left ,a,x)
                dfs(n.right,x,b)
        dfs(root,-Inf,Inf)
        return self.best