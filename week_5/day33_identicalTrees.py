"""
Given two binary trees, return whether or not the two trees are identical. Note: identical meaning they exhibit the same structure and the same values at each node. Ex: Given the following trees...

        2
       / \
      1   3
    2
   / \
  1   3

return true.

Ex: Given the following trees...

        1
         \
          9
           \
           18
    1
   /
  9
   \
    18

return false.

Ex: Given the following trees...

        2
       / \
      3   1
    2
   / \
  1   3

return false.   
"""
class BST():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# Time O(n)
# Space O(n)
def is_same_tree(t1, t2):
    if t1 and not t2 or t2 and not t1:
        return False
    elif not t1 and not t2:
        return True
    
    left = is_same_tree(t2.left, t1.left)
    
    if t1.value != t2.value:
        return False
    
    right = is_same_tree(t2.right, t1.right)
    
    return left and right

# refactored

def is_same_tree(t1, t2):
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    
    if t1.value != t2.value:
        return False

    return is_same_tree(t2.left, t1.left) and \
        is_same_tree(t2.right, t1.right)