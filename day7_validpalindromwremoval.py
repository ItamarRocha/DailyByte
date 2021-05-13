"""
This question is asked by Facebook. Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

    "abcba", return true
    "foobof", return true (remove the first 'o', the second 'o', or 'b')
    "abccab", return false
"""

# Time O(n). Although it seems to have a loop inside another loop, which would incorrectly lead
# to assuming that it is O(n^2), we only pass through the entirity of the string once or twice
# in the worst case, where the first letter is different O(2n).

# Space O(1)
def is_palindrome(string, start, end):
    while start<=end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

def palindrom_w_removal(string):
    start = 0
    end = len(string) - 1
    
    while start <= end:
        if string[start] != string[end]:
            return is_palindrome(string, start+1,end) or is_palindrome(string, start, end-1)
        start += 1
        end -= 1
    return True

print(palindrom_w_removal("abcba"))
print(palindrom_w_removal("foobof"))
print(palindrom_w_removal("abccab")) 