"""
This question is asked by Amazon. Given two strings s and t, which represents a sequence of keystrokes, where # denotes a backspace, return whether or not the sequences produce the same result.

Ex: Given the following strings...

    s = "ABC#", t = "CD##AB", return true
    s = "como#pur#ter", t = "computer", return true
    s = "cof#dim#ng", t = "code", return false
"""

# Approach 1
# Time O(m + n)
# Space O(m + n)
def resolve_string(s):
    stack = []

    for el in s:
        if el == "#":
            if stack:
                stack.pop()
        else:
            stack.append(el) 
    return "".join(stack)
            
def compare_key_strokes(s,t):
    return resolve_string(s) == resolve_string(t)

print(compare_key_strokes("ABC#","CD##AB"))
print(compare_key_strokes("como#pur#ter","computer"))
print(compare_key_strokes("cof#dim#ng","code"))
print(compare_key_strokes("cof#dim#ng","coding"))
print(compare_key_strokes("y#fo##f","y#f#o##f"))

# Approach 2
# Time O(m + n)
# Space O(1)
print("\n\nApproach 2:\n")

def compare_key_strokes(s,t):
    i = len(s) - 1 
    j = len(t) - 1

    skip_i = 0
    skip_j = 0

    while i >= 0 or j >= 0:
        if i >= 0 and s[i] == "#":
            skip_i += 1
            i -= 1
            continue
        if j >= 0 and t[j] == "#":
            skip_j += 1
            j -= 1
            continue

        if i >= 0 and skip_i > 0:
            i -= 1
            skip_i -= 1
            continue

        if j >= 0 and skip_j > 0:
            j -= 1
            skip_j -= 1
            continue
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False
        i -= 1
        j -= 1

    return True if i == j else False

print(compare_key_strokes("ABC#","CD##AB"))
print(compare_key_strokes("como#pur#ter","computer"))
print(compare_key_strokes("cof#dim#ng","code"))
print(compare_key_strokes("cof#dim#ng","coding"))
print(compare_key_strokes("y#fo##f","y#f#o##f"))
