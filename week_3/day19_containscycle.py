"""
This question is asked by Microsoft. Given a linked list, containing unique numbers, return whether or not it has a cycle.
Note: a cycle is a circular arrangement (i.e. one node points back to a previous node)

Ex: Given the following linked lists...

    1->2->3->1 -> true (3 points back to 1)
    1->2->3 -> false
    1->1 true (1 points to itself)
"""
print("First solution\n")
class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

# First solution
# Time O(n) Space O(n)
def contains_cycle(head):
    seen_nodes = set()

    cur = head

    while cur:
        if cur.value in seen_nodes:
            return True
        seen_nodes.add(cur.value)
        cur = cur.next

    return False

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)
l1.next.next.next = l1

print(contains_cycle(l1))

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)

print(contains_cycle(l1))

l1 = LinkedList(1)
l1.next = l1

print(contains_cycle(l1))

# Second solution
# modify the data structure
# Time O(n) Space O(1)
print("Second solution\n")
class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.visited = False

def contains_cycle(head):
    cur = head

    while cur:
        if cur.visited:
            return True
        cur.visited = True
        cur = cur.next

    return False

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)
l1.next.next.next = l1

print(contains_cycle(l1))

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)

print(contains_cycle(l1))

l1 = LinkedList(1)
l1.next = l1

print(contains_cycle(l1))


# Third solution
# Two pointers
# Time O(n) Space O(1)
print("Third solution\n")
class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

def contains_cycle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)
l1.next.next.next = l1

print(contains_cycle(l1))

l1 = LinkedList(1)
l1.next = LinkedList(2)
l1.next.next = LinkedList(3)

print(contains_cycle(l1))

l1 = LinkedList(1)
l1.next = l1

print(contains_cycle(l1))
