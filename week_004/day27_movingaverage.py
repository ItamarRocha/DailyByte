"""
This question is asked by Microsoft. Design a class, MovingAverage, which contains a method, next that is responsible for returning the moving average from a stream of integers.
Note: a moving average is the average of a subset of data at a given point in time.

Ex: Given the following series of events...

    // i.e. the moving average has a capacity of 3.
    MovingAverage movingAverage = new MovingAverage(3);
    m.next(3) returns 3 because (3 / 1) = 3
    m.next(5) returns 4 because (3 + 5) / 2 = 4 
    m.next(7) = returns 5 because (3 + 5 + 7) / 3 = 5
    m.next(6) = returns 6 because (5 + 7 + 6) / 3 = 6
"""
# Time O(n)
# Space O(n)
class MovingAverage():
    def __init__(self, window):
        self.counter = 0
        self.queue = [None] * window
    
    def next(self, new_value):
        self.counter += 1
        
        self.queue.pop(0)
        self.queue.append(new_value)

        total = self.queue[-self.counter:] if self.counter < len(self.queue) else self.queue
        print(total, self.queue)
        return sum(total)/len(total)

m = MovingAverage(3)

print(m.next(3))
print(m.next(5))
print(m.next(7))
print(m.next(6))

# Time O(1)
# Space O(n)
class MovingAverage():
    def __init__(self, window):
        self.counter = 0
        self.window = window
        self.queue = [None] * window
        self.mean = 0

    def next(self, new_value):
        self.counter += 1
        
        popped_el = self.queue.pop(0)
        self.queue.append(new_value)

        last_mean = self.mean

        if self.counter <= self.window:
            self.mean = (last_mean * (self.counter-1) + new_value) / self.counter
        else:
            self.mean = (last_mean * (self.window) - popped_el + new_value)/self.window
        print(self.queue)
        return self.mean

m = MovingAverage(3)

print(m.next(3))
print(m.next(5))
print(m.next(7))
print(m.next(6))