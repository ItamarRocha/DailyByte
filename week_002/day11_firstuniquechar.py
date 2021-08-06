"""
This question is asked by Microsoft. Given a string, return the index of its first unique character. If a unique character does not exist, return -1.

Ex: Given the following strings...

    "abcabd", return 2
    "thedailybyte", return 1
    "developer", return 0
"""
#Time O(n)
#Space O(1) (we have a limited set of chars, but for small strings we can consider O(n))
def get_first_unique_char(string):
    char_count = {}

    for el in string:
        if el not in char_count:
            char_count[el] = 1
        else:
            char_count[el] += 1
    
    for i in range(len(string)):
        if char_count[string[i]] == 1:
            return i
    
    return -1

print(get_first_unique_char("abcabd"))
print(get_first_unique_char("thedailybyte"))
print(get_first_unique_char("developer"))
print(get_first_unique_char("devdev"))