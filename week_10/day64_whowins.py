"""
This question is asked by Amazon. Given an integer array, two players take turns picking the largest number 
from the ends of the array. First, player one picks a number (either the left end or right end of the array)
 followed by player two. Each time a player picks a particular numbers, it is no longer available to the other
  player. This picking continues until all numbers in the array have been chosen. Once all numbers have been 
  picked, the player with the larger score wins. Return whether or not player one will win.
Note: You may assume that each player is playing to win (i.e. both players will always choose the maximum of
 the two numbers each turn) and that there will always be a winner.

Ex: Given the following integer array...

nums = [1, 2, 3], return true
Player one takes 3
Player two takes 2
Player one takes 1
3 + 1 > 2 and therefore player one wins
https://leetcode.com/problems/predict-the-winner
"""
# Time O(n²)
# Space O(n²)
def whowins(nums):
    return winner(nums,0,len(nums)-1, {}) >= 0

def winner(nums, s, e, memo):
    if s == e:
        return nums[s]
    if (s,e) in memo:
        return memo[(s,e)]
    
    a = nums[s] - winner(nums, s+1, e, memo)
    b = nums[e] - winner(nums, s, e-1, memo)
    
    memo[(s,e)] = max(a,b)
    return memo[(s,e)]

print(whowins([1,2,3]))