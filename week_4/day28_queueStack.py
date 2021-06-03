"""
Design a class to implement a stack using only a single queue. Your class, QueueStack, should support the following 
stack methods: push() (adding an item), pop() (removing an item), peek() (returning the top value without removing
 it), and empty() (whether or not the stack is empty).
"""
class QueueStack():
    def __init__(self):
        self.queue = []
    
    def empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.empty():
            return None
        return self.queue[-1]

    def push(self, value):
        self.queue.append(value)
    
    # Time O(n)
    # Makes the pop operation costly in order to simulate a stack with a queue
    # pops the element and then send to the end of the queue while is not the
    # desired "last" element.
    def pop(self):
        value_to_pop = self.peek()

        if not value_to_pop:
            return None

        popped_value = self.queue.pop(0)

        while popped_value != value_to_pop:
            self.queue.append(popped_value)
            popped_value = self.queue.pop(0)
        
        return popped_value

qs = QueueStack()
print(qs.empty())
print(qs.peek())

qs.push(10)
qs.push(12)
qs.push(13)

print(qs.queue)
print(qs.pop()) # remove 13
print(qs.queue)
print(qs.peek()) # 12

print(qs.pop()) # remove 12
print(qs.queue)

print(qs.pop()) # remove 10
print(qs.queue)

print(qs.pop()) # has nothing left to remove
print(qs.queue)