"""
This question is asked by Google. Given two strings s and t return whether or not s is a subsequence of t.
Note: You may assume both s and t only consist of lowercase characters and both have a length of at least one.

Ex: Given the following strings s and t…

s = "abc", t = "aabbcc", return true.
Ex: Given the following strings s and t…

s = "cpu", t = "computer", return true.
Ex: Given the following strings s and t…

s = "xyz", t = "axbyc", return false.
"""
# Time O(n)
# Space O(n)
def is_subsequence(s,t):
    reversed_s = s[::-1]
    order = [c for c in reversed_s]

    i = 0
    while i < len(t):
        if not order:
            break

        if t[i] == order[-1]:
            order.pop()
        
        i+=1
    
    return len(order) == 0

print(is_subsequence("abc", "aabbcc")) # true
print(is_subsequence("cpu", "computer")) # true
print(is_subsequence("xyz", "axbyc")) # false
print(is_subsequence("abc", "ahbgdc")) # true
print(is_subsequence("axc", "ahbgdc")) # false

print("\nOptimized sol :")
# Time O(n)
# Space O(1)
def is_subsequence(s,t):
    s_cursor = 0
    i = 0
    while i < len(t):
        if s_cursor == len(s):
            break

        if t[i] == s[s_cursor]:
            s_cursor += 1
        
        i+=1
    
    return s_cursor == len(s)

print(is_subsequence("abc", "aabbcc")) # true
print(is_subsequence("cpu", "computer")) # true
print(is_subsequence("xyz", "axbyc")) # false
print(is_subsequence("abc", "ahbgdc")) # true
print(is_subsequence("axc", "ahbgdc")) # false