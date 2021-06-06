"""
Given a binary search tree, rearrange the tree such that it forms a linked list where all its values are in ascending order.

Ex: Given the following tree...
        5
       / \
      1   6
return...

1
 \
  5
   \
    6
Ex: Given the following tree...

       5
      / \
    2    9
   / \ 
  1   3 
return...

1
 \
  2
   \
    3
     \
      5
       \
        9
Ex: Given the following tree...

5
 \
  6
return...

5
 \
  6
"""
class BST():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(input_list):
    linked_list = ""
    while input_list:
        linked_list += str(input_list.value) + "->"
        input_list=input_list.next
    if len(linked_list):
        linked_list = linked_list[:-2]
    print(linked_list)

root = BST(5)
root.left = BST(1)
root.right = BST(6)

def convert(root):
    if not root:
        return None
    
    head = LinkedList(-1)
    cursor = head

    helper(root, cursor)

    return head.next

def helper(root, cursor):
    if not root:
        return

    helper(root.left, cursor)
    
    print("root : ", root.value)
    print("cursor : ", cursor.value if cursor else cursor)
    cursor.next = LinkedList(root.value)
    cursor = cursor.next

    helper(root.right, cursor)

    return

root = BST(5)
root.left = BST(2)
root.right = BST(9)
root.left.left = BST(1)
root.left.right = BST(3)

print_list(convert(root))