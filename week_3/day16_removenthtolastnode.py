"""
This question is asked by Facebook. Given a linked list and a value n, remove the nth to last node and return the resulting list.

Ex: Given the following linked lists...

    1->2->3->null, n = 1, return 1->2->null
    1->2->3->null, n = 2, return 1->3->null
    1->2->3->null, n = 3, return 2->3->null
"""
class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

def get_listlength(llist):
    length = 0

    while llist:
        llist = llist.next
        length += 1
    
    return length

# Time O(n)
# Space O(1)
def removenthlastnode(llist, n):
    list_length = get_listlength(llist)
    node_to_remove = list_length - n
    node_count = 0

    head = LinkedList(-1)
    head.next = llist

    previous = head

    while llist:
        if node_count == node_to_remove:
            previous.next = llist.next
            break
        previous = llist
        llist = llist.next
        node_count += 1
    
    return head.next

def print_list(merged_list):
    while merged_list:
        print(merged_list.value)
        merged_list=merged_list.next

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)

list_removed = removenthlastnode(l1, 1)
print_list(list_removed)

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)

list_removed = removenthlastnode(l1, 2)
print_list(list_removed)

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)

list_removed = removenthlastnode(l1, 3)
print_list(list_removed)
