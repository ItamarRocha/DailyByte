"""
This question is asked by Google. Given a staircase with N steps and the ability to climb
 either one or two steps at a time, return the total number of ways to arrive at the top 
 of the staircase.

Ex: Given the following value of N…

N = 2, return 2
1 step + 1 step
2 steps
Ex: Given the following value of N…

N = 3, return 3
1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
"""
# Time O(2^n)
# Space O(N) #callstack height
def n_steps(N):
    if N == 0:
        return 1
    elif N < 0:
        return 0

    return n_steps(N-1) + n_steps(N-2)

print(n_steps(2))
print(n_steps(3))
print(n_steps(4))
print(n_steps(5))

# Time O(N)
# Space O(N)
def n_steps(N, memo={}):
    if N == 0:
        return 1
    elif N < 0:
        return 0

    if N in memo:
        return memo[N]

    memo[N] = n_steps(N-1) + n_steps(N-2)
    return memo[N]

print(n_steps(2))
print(n_steps(3))
print(n_steps(4))
print(n_steps(5))

# Time O(N)
# Space O(1)
def n_steps(N):
    if N == 1:
        return 1
    
    first = 1
    second = 2

    for i in range(3,N+1):
        third = first + second
        first = second
        second = third
    
    return second

print(n_steps(2))
print(n_steps(3))
print(n_steps(4))
print(n_steps(5))