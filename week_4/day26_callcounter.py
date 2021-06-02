"""
This question is asked by Google. Create a class CallCounter that tracks the number of calls a client has made within the last 3 seconds. Your class should contain one method, ping(int t) that receives the current timestamp (in milliseconds) of a new call being made and returns the number of calls made within the last 3 seconds.
Note: you may assume that the time associated with each subsequent call to ping is strictly increasing.

Ex: Given the following calls to ping…

    ping(1), return 1 (1 call within the last 3 seconds)
    ping(300), return 2 (2 calls within the last 3 seconds)
    ping(3000), return 3 (3 calls within the last 3 seconds)
    ping(3002), return 3 (3 calls within the last 3 seconds)
    ping(7000), return 1 (1 call within the last 3 seconds)
"""
# Time O(n)
# Space O(n)
class callCounter():
    def __init__(self):
        self.pings = set()

    def count_last3(self, current):
        low_interval = current - 3000
        low_interval = low_interval if low_interval >= 0 else 0
        returned = []

        for value in self.pings:
            if low_interval <= value <= current:
                returned.append(value)
        
        return returned

    def ping(self, time):
        self.pings.add(time)
        return len(self.count_last3(time))
    
cc = callCounter()

print(cc.ping(1))
print(cc.ping(300))
print(cc.ping(3000))
print(cc.ping(3002))
print(cc.ping(7000))
