"""
This question is asked by Facebook. Given a string s containing only lowercase letters, continuously remove adjacent characters that are the same and return the result.

Ex: Given the following strings...

    s = "abccba", return ""
    s = "foobar", return "fbar"
    s = "abccbefggfe", return "a"
"""
# Time O(n)
# Space O(n)
def removeadjacentduplicates(s):
    stack = []
    for el in s:
        if stack and stack[-1] == el:
            stack.pop()
            continue
        stack.append(el)

    return "".join(stack)

print(removeadjacentduplicates("abccba"))
print(removeadjacentduplicates("foobar"))
print(removeadjacentduplicates("abccbefggfe"))
