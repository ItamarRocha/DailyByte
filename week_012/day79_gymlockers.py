"""
This question is asked by Facebook. In a gym hallway there are N lockers. 
You walk back and forth down the hallway opening and closing lockers. On your first pass 
you open all the lockers. On your second pass, you close every other locker. On your third 
pass you open every third locker. After walking the hallway N times opening/closing lockers 
in the previously described manner, how many locker are left open?

Ex: Given the following value of N…

N = 1, return 1.
You walk down the hallway once and open the only locker.
Ex: Given the following value of N…

N = 2, return 1.
You walk down the hallway and open both lockers.
You walk back down the hallway and close the last locker.
https://leetcode.com/problems/bulb-switcher/
"""
# Time O(sqrt(N) * N)
# Space O(N)
def gymlockers(N):
    lockers_divisors = [2] * (N + 1)
    lockers_divisors[1] = 1
    
    i = 2
    
    while i * i <= N:
        for j in range(i+i, N+1, i):
            lockers_divisors[j] += 1
            if i * i != j:
                lockers_divisors[j] += 1
        i += 1
    
    open_lockers = 0

    for i in range(1, N+1):
        if lockers_divisors[i] % 2 == 1:
            open_lockers += 1
    
    return open_lockers

from math import sqrt
def gymlockers(N):
    return int(sqrt(N))

print(gymlockers(1))
print(gymlockers(2))
print(gymlockers(999999))