"""
This question is asked by Google. Given a linked list and a value, remove all nodes containing the provided value, and return the resulting list.

Ex: Given the following linked lists and values...

    1->2->3->null, value = 3, return 1->2->null
    8->1->1->4->12->null, value = 1, return 8->4->12->null
    7->12->2->9->null, value = 7, return 12->2->9->null
"""
class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

# Time O(n)
# Space O(1)
def remove_value(head, value):
    new_head = LinkedList(-1)
    new_head.next = head

    previous = new_head
    cur = head

    while cur:
        if cur.value == value:
            previous.next = cur.next
        else:
            previous = cur
        cur = cur.next
    return new_head.next

def print_list(merged_list):
    linked_list = ""
    while merged_list:
        linked_list += str(merged_list.value) + "->"
        merged_list=merged_list.next
    if len(linked_list):
        linked_list = linked_list[:-2]
    print(linked_list)

# Ex1: 1->2->3->null, value = 3, return 1->2->null
l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)

new_list = remove_value(l1, 3)
print_list(new_list)

# Ex2: 8->1->1->4->12->null, value = 1, return 8->4->12->null
l2 = LinkedList(8)
l2.next = LinkedList(1)
l2.next.next = LinkedList(1)
l2.next.next.next = LinkedList(4)
l2.next.next.next.next = LinkedList(12)

new_list = remove_value(l2, 1)
print_list(new_list)

# Ex3: 7->12->2->9->null, value = 7, return 12->2->9->null

l3 = LinkedList(7)
l3.next = LinkedList(12)
l3.next.next = LinkedList(2)
l3.next.next.next = LinkedList(9)

new_list = remove_value(l3, 7)
print_list(new_list)