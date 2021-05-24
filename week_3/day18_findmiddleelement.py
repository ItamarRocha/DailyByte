"""
This question is asked by Amazon. Given a non-empty linked list, return the middle node of the list. If the linked list contains an even number of elements, return the node closer to the end.


    1->2->3->null, return 2
    1->2->3->4->null, return 3
    1->null, return 1
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

def find_middle_element(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)

print(find_middle_element(l1).value)

l2 = LinkedList(1)
l2.next = LinkedList(2)
l2.next.next = LinkedList(3)
l2.next.next.next = LinkedList(4)

print(find_middle_element(l2).value)

l3 = LinkedList(1)

print(find_middle_element(l3).value)