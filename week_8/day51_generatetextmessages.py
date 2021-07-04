"""
This question is asked by Google. Given a string of digits, return all possible text messages those
 digits could send. Note: The mapping of digits to letters is as follows…

0 -> null
1 -> null
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"
Ex: digits = "23" return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

d = {"0":None, "1":None, "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
# Time O(4^n)
# Space O(4^n)
def helper(string, i, cur_string, output):
    if i == len(string):
        output.append(cur_string)
        return
    for el in d[string[i]]:
        if el:
            helper(string, i + 1, cur_string + el, output)
    return

def generate(string):
    output = []
    helper(string, 0 , "", output)
    return output

print(generate("23"))

def generate2(string, output=[]):
    if len(string) == 0:
        return [""]
    
    sub_strs = generate2(string[1:], output)

    for el in d[string[0]]:
        for sub_str in sub_strs:
            output.append(el + sub_str)
    
    return output

print(generate("23"))