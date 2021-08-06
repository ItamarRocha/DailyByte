"""
This question is asked by Apple. Given two sorted linked lists, merge them together in ascending order and return a reference to the merged list

Ex: Given the following lists...

    list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
    list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
    list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null
"""
class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

# Time O(n + m)
# Space O(1)
def merge_linkedlists(list1, list2):
    head = LinkedList(-1)
    cur = head

    while list1 != None and list2 != None:
        if list1.value < list2.value:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    
    cur.next = list1 if list1 != None else list2

    return head.next

def print_list(merged_list):
    while merged_list:
        print(merged_list.value)
        merged_list=merged_list.next

# Ex 1
print("EX 1")

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)

l2 = LinkedList(4)
l2.next = LinkedList(5)
l2.next.next = LinkedList(6)

merged_list = merge_linkedlists(l1,l2)

print_list(merged_list)

# Ex 2
print("EX 2")

l1 = LinkedList(1)
l1.next = LinkedList(3)
l1.next.next = LinkedList(5)

l2 = LinkedList(2)
l2.next = LinkedList(4)
l2.next.next = LinkedList(6)

merged_list = merge_linkedlists(l1,l2)

print_list(merged_list)

# Ex 3
print("EX 3")

l1 = LinkedList(4)
l1.next = LinkedList(4)
l1.next.next = LinkedList(7)

l2 = LinkedList(1)
l2.next = LinkedList(5)
l2.next.next = LinkedList(6)

merged_list = merge_linkedlists(l1,l2)

print_list(merged_list)