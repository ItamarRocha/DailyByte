"""
This question is asked by Amazon. Given a string s consisting of only letters and digits,
 where we are allowed to transform any letter to uppercase or lowercase, return a list 
 containing all possible permutations of the string.

Ex: Given the following string…

S = "c7w2", return ["c7w2", "c7W2", "C7w2", "C7W2"]
"""
# Time O(2^n)
# Space O(2^n)
def string_permutations(s):
    output = []

    generate(s, 0, output)

    return output

def generate(s, i, output):
    if i == len(s):
        output.append(s)
        return

    if s[i].isalpha():
        formed_string1 = s[:i] + s[i].lower() + s[i+1:]
        generate(formed_string1, i + 1, output)

        formed_string2 = s[:i] + s[i].upper() + s[i+1:]
        generate(formed_string2, i + 1, output)
    else:
        generate(s, i+1, output)

print(string_permutations("c7w2"))