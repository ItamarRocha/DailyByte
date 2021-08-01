"""
This question is asked by Facebook. Given a string, reverse the vowels of it.
Note: In this problem y is not considered a vowel.

Ex: Given the following strings s…

s = "computer", return "cemputor"
Ex: Given the following strings s…

s = "The Daily Byte", return "The Dialy Byte"
"""
# Time O(n)
# Space O(n)
def reverse_vowels(string):
    vowels = set(["a","e","i","o","u"])
    string = list(string)

    l = 0
    r = len(string)-1

    while l <= r:
        if string[l].lower() not in vowels:
            l +=1
        elif string[r].lower() not in vowels:
            r -= 1
        else:
            string[l], string[r] = string[r], string[l]
            l+=1
            r -= 1
    
    return "".join(string)

print(reverse_vowels("computer"))
print(reverse_vowels("The Daily Byte"))