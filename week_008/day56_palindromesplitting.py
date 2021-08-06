"""
This question is asked by Google. Given a string s, return all possible partitions of s such that each substring is a palindrome.

Ex: Given the following string s…

s = "abcba",
return [
    ["a","b","c","b","a"],
    ["a","bcb","a"],
    ["abcba"]
]
"""
# Time O(???) # two loops and the inversion
# space O(???)
def palindrome_splitting(s):
    output = []
    splitter(s, output)
    return output

def splitter(s, output, cur_things=[]):
    if len(s) == 0:
        output.append(cur_things)
        return output

    for i in range(1,len(s)+1):
        # print(i, s[:i])
        if s[:i] == s[:i][::-1]:
            splitter(s[i:], output, cur_things + [s[:i]])

    return output


print(palindrome_splitting("abcba"))