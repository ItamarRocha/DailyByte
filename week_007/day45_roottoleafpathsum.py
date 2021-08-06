"""
Given a binary tree and a target, return whether or not there exists a root to leaf path such that all values along the path sum to the target.

Ex: Given the following tree…

      1
     / \
    5   2
   /   / \
  1  12   29
and a target of 15, return true as the path 1->2->12 sums to 15.
Ex: Given the following tree…

     104
    /   \
  39     31
 / \    /  \
32  1  9    10
and a target of 175, return true as the path 104->39->32 sums to 175.
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time O(n) (do the traverse is O(n), reverse the string is O(n), 
# joining the string is also O(n), but they are done separately)
# Space O(n) (we are creating the res, and using the call stack)
def root_to_leaf_pathsum(root, targetSum):
    res = []

    helper(root, targetSum, 0, res)
    return "->".join(res[::-1])

def helper(root, target, cur_sum, res=[]):
    if not root: return
    
    if not root.left and not root.right and cur_sum + root.value == target:
        res.append(str(root.value))
        return True
    
    left = helper(root.left, target, cur_sum + root.value, res)
    right = helper(root.right, target, cur_sum + root.value, res)
    
    if left or right:
        res.append(str(root.value))
    return left or right

root = Tree(1)
root.left = Tree(5)
root.left.right = Tree(1)
root.right = Tree(2)
root.right.left = Tree(12)
root.right.right = Tree(29)

print(root_to_leaf_pathsum(root, 15))