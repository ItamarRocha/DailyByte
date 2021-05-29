"""
This question is asked by Google. Given a string only containing the following characters (, ), {, }, [, and ] return whether or not the opening and closing characters are in a valid order.

Ex: Given the following strings...

    "(){}[]", return true
    "(({[]}))", return true
    "{(})", return false
"""
# Time O(n)
# Space O(n)
def validate_characters(string):
    correspondence = {"(": ")", "[":"]", "{":"}"}
    stack = []

    for el in string:
        if el in correspondence.keys():
            stack.append(el)
        elif len(stack) > 0:
            if correspondence[stack[-1]] == el:
                stack.pop()
            else:
                return False
        else:
            return False
    
    return True if len(stack) == 0 else False

print(validate_characters("(){}[]"))
print(validate_characters("(({[]}))"))
print(validate_characters("{(})"))
print(validate_characters("{"))

# Refactored solution
def validate_characters(string):
    correspondence = {"(": ")", "[":"]", "{":"}"}
    stack = []

    for el in string:
        if el in correspondence.keys():
            stack.append(el)
        elif stack and correspondence[stack[-1]] == el:
                stack.pop()
        else:
            return False
    
    return stack == []

print(validate_characters("(){}[]"))
print(validate_characters("(({[]}))"))
print(validate_characters("{(})"))
print(validate_characters("{"))