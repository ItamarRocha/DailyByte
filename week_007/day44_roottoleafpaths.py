"""
Given a binary tree, return a list of strings containing all root to leaf paths.

Ex: Given the following tree…

   1
 /   \
2     3
return ["1->2", "1->3"]
Ex: Given the following tree…

    8
   / \
  2  29
    /  \
   3    9
return ["8->2", "8->29->3", "8->29->9"]
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time O(n²) # extend is O(n)
# Space O(n)
def roottoleafpaths(root):
    if not root:
        return []

    if not root.left and not root.right:
        return [str(root.value)]
    
    output = roottoleafpaths(root.left)
    output.extend(roottoleafpaths(root.right))

    output = list(map(lambda x: str(root.value) + "->" + x, output))

    return output

# time O(n)
# Space O(2n)
def create_str(string, val):
    if string == "":
        return str(val)
    return string + "->" + str(val)

def roottoleafpaths(root, res=[], cur_str=""):
    if not root:
        return

    new_str = create_str(cur_str, root.value)
    
    if not root.left and not root.right:
        res.append(new_str)
    
    roottoleafpaths(root.left, res, new_str)
    roottoleafpaths(root.right, res, new_str)

    return res

# Time O(n)
# Time O(n)
def roottoleafpaths(root):
    output = []
    binaryPaths(root, [], output)
    return output

def binaryPaths(root, currEl, output):
    if root is None:
        return

    # add the root.val to currEl
    currEl.append(str(root.value))

    if root.left is None and root.right is None:
        stringOutput = ''.join(currEl) 
        output.append(stringOutput)
        currEl.pop()
        return 

    currEl.append("->") 

    if root.left:
        binaryPaths(root.left, currEl, output)

    if root.right:
        binaryPaths(root.right, currEl, output)

    currEl.pop()
    currEl.pop()

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)

print(roottoleafpaths(root))

root = Tree(8)
root.left = Tree(2)
root.right = Tree(29)
root.right.left = Tree(3)
root.right.right = Tree(9)

print(roottoleafpaths(root))

root = Tree(1)
root.left = Tree(2)
root.left.right = Tree(5)
root.right = Tree(3)

print(roottoleafpaths(root))