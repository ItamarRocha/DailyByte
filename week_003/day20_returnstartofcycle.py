"""
This question is asked by Apple. Given a potentially cyclical linked list where each value is unique, return the node at which the cycle starts. If the list does not contain a cycle, return null.

Ex: Given the following linked lists...

    1->2->3, return null
    1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
    1->9->3->7->7 (7 points to itself), return a reference to the node containing 7
"""
class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

def tests(startofcycle):
    # test 1
    l1 = LinkedList(1)
    l1.next = LinkedList(2)
    l1.next.next = LinkedList(3)

    print(startofcycle(l1))

    # test 2
    l1 = LinkedList(1)
    l1.next = LinkedList(2)
    l1.next.next = LinkedList(3)
    l1.next.next.next = LinkedList(4)
    l1.next.next.next.next = LinkedList(5)
    l1.next.next.next.next.next = l1.next

    print(startofcycle(l1))

    # test 3
    l1 = LinkedList(1)
    l1.next = LinkedList(9)
    l1.next.next = LinkedList(3)
    l1.next.next.next = LinkedList(7)
    l1.next.next.next.next = l1.next.next.next
    print(startofcycle(l1))

# Time O(n)
# Space O(n)
def startofcycle(head):
    seen_nodes = set()

    cur = head

    while cur:
        if cur in seen_nodes:
            return (cur, cur.value)
        seen_nodes.add(cur)
        cur = cur.next
    
    return None

# Time O(n)
# Space O(1)
def startofcycle2(head):
    # D -> distance between start and beggining of loop
	# P -> distance between beggining of loop and encounter node
	# distance traveled by cursor_1 = D + P 
	# distance traveled by cursor_2 = 2D + 2P
	# Total distance = 2D + P
	# Distance from encounter node to beggining of loop = [D + P] + D (so we can meet the final distance)
	# to reach D we just need to place cursor_1 at the beggining and let them walk at the same pace :)
	# till they find each other
    first = head.next
    second = head.next.next

    while second and second.next and first != second:
        first = first.next
        second = second.next.next
    
    second = head

    while first and second and first != second:
        first = first.next
        second = second.next
    
    return (first, first.value) if first == second else None

tests(startofcycle)
tests(startofcycle2)