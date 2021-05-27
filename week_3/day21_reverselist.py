"""
This question is asked by Facebook. Given a linked list, containing unique values, reverse it, and return the result.

Ex: Given the following linked lists...

    1->2->3->null, return a reference to the node that contains 3 which points to a list that looks like the following: 3->2->1->null
    7->15->9->2->null, return a reference to the node that contains 2 which points to a list that looks like the following: 2->9->15->7->null
    1->null, return a reference to the node that contains 1 which points to a list that looks like the following: 1->null
"""
class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(merged_list):
    linked_list = ""
    while merged_list:
        linked_list += str(merged_list.value) + "->"
        merged_list=merged_list.next
    if len(linked_list):
        linked_list = linked_list[:-2]
    print(linked_list)

def tests(reverse_list):
    # test 1
    l1 = LinkedList(1)
    l1.next = LinkedList(2)
    l1.next.next = LinkedList(3)

    new_ll = reverse_list(l1)
    print_list(new_ll)

    # test 2
    l1 = LinkedList(7)
    l1.next = LinkedList(15)
    l1.next.next = LinkedList(9)
    l1.next.next.next = LinkedList(2)

    new_ll = reverse_list(l1)
    print_list(new_ll)

    # test 3
    l1 = LinkedList(1)
    new_ll = reverse_list(l1)
    print_list(new_ll)

# Space O(1)
# Time O(n)
def reverse_list(head):
    new_head = head
    previous = None
    cur = head

    while cur:
        new_head = cur
        
        cur = cur.next
        new_head.next = previous            

        previous = new_head

    return new_head

tests(reverse_list)