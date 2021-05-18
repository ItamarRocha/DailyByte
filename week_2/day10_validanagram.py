"""
This question is asked by Facebook. Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

    Ex: Given the following strings...

    s = "cat", t = "tac", return true
    s = "listen", t = "silent", return true
    s = "program", t = "function", return false
"""

# Time O(s) -> s being length of s
# Space O(s)
def valid_anagram(s,t):
    if len(s) != len(t):
        return False

    s_char_count = {}

    for el in s:
        if el not in s_char_count:
            s_char_count[el] = 1
        else:
            s_char_count[el] += 1
    
    for el in t:
        if el not in s_char_count or s_char_count[el] <= 0:
            return False
        else:
            s_char_count[el] -= 1
    
    for el in s:
        if s_char_count[el] != 0:
            return False
    
    return True

print(valid_anagram("cat", "tac"))
print(valid_anagram("listen", "silent"))
print(valid_anagram("program", "function"))
print(valid_anagram("ab", "a"))