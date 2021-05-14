"""
This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

    "level", return true
    "algorithm", return false
    "A man, a plan, a canal: Panama.", return true
"""

# Time O(n) n->number of chars in str1
# Space O(1)
# We could, instead of using the str.lower, check if it is in another range, and then decrease the corresponding value
def is_palindrome(str1):
    i = 0
    j = len(str1) - 1
    
    str1 = str1.lower() # remove the Upper cases

    while i <= j:
        if not is_in_range(str1[i]):
            i += 1
            continue
        elif not is_in_range(str1[j]):
            j -= 1
            continue

        if str1[i] == str1[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

# Time O(1)
# Space O(1)
def is_in_range(char1):
    if 97 <= ord(char1) <= 122:
        return True
    return False

assert is_palindrome("level") == True
assert is_palindrome("algorithm") == False
assert is_palindrome("A man, a plan, a canal: Panama.") == True
