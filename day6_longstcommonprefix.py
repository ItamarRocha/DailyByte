"""
This question is asked by Microsoft. Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

    ["colorado", "color", "cold"], return "col"
    ["a", "b", "c"], return ""
    ["spot", "spotty", "spotted"], return "spot"
"""

# Time O(n * m) -> n is the number os strings and m is the max number of chars in a string
# Space O(m)
def longest_common_prefix(strings):
    prefix = strings[0]
    for i in range(1,len(strings)):
        cur_prefix = prefix
        prefix = ""
        for c1, c2 in zip(cur_prefix, strings[i]):
            if c1 != c2:
                break
            prefix += c1
    
    return prefix

print(longest_common_prefix(["colorado", "color", "cold"]))
print(longest_common_prefix(["a", "b", "c"]))
print(longest_common_prefix(["spot", "spotty", "spotted"]))