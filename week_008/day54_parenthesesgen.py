"""
This question is asked by Facebook. Given an integer N, where N represents the number 
of pairs of parentheses (i.e. ”(“ and ”)”) you are given, return a list containing all 
possible well-formed parentheses you can create.

Ex: Given the following value of N…

N = 3, 
return [  
    "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
# Time O(2^n)
# Space O(2^n)
def generate_parentheses(n):
    output = []

    generator(n,n,output, "")

    return output

def generator(i,j, output, cur_str):
    if j < i or i < 0 or j < 0:
        return

    if i == j == 0:
        output.append(cur_str)
        return

    generator(i-1,j, output, cur_str + "(")
    generator(i,j-1, output, cur_str + ")")

    return

print(generate_parentheses(3))