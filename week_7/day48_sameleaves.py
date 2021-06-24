"""
Given two binary trees, return whether or not both trees have the same leaf sequence. Two trees have the same leaf sequence if both trees’ leaves read the same from left to right.

Ex: Given the following trees…

   1
 /   \
1     3
and


   7
 /   \
1     2
return false as both the trees' leaves don't read the same from left to right (i.e. [1, 3] and [1, 2]).

Ex: Given the following trees…

    8
   / \
  2   29
    /  \
   3    9
and

    8
   / \
  2  29
 /   /  \
2   3    9
     \
      3
return true as both the trees' leaves read the same from left to right (i.e. [2, 3, 9] and [2, 3, 9]).
"""
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sameleaves(root1, root2):

    output1 = []
    output2 = []

    get_leaves(root1, output1)
    get_leaves(root2, output2)

    if len(output1) != len(output2):
        return False

    
    for el1,el2 in zip(output1, output2):
        if el1 != el2:
            return False

    return True

    
def get_leaves(node, output):

    if not node:
        return

    if not node.left and not node.right:
        output.append(node.value)
    
    get_leaves(node.left, output)
    get_leaves(node.right, output)

    return

root1 = Tree(1)
root1.left = Tree(1)
root1.right = Tree(3)

root2 = Tree(7)
root2.left = Tree(1)
root2.right = Tree(2)

print(sameleaves(root1,root2))

root1 = Tree(8)
root1.left = Tree(2)
root1.right = Tree(29)
root1.right.left = Tree(3)
root1.right.right = Tree(9)

root2 = Tree(8)
root2.left = Tree(2)
root2.left.left = Tree(2)
root2.right = Tree(29)
root2.right.left = Tree(3)
root2.right.left.right = Tree(3)
root2.right.right = Tree(9)

print(sameleaves(root1,root2))