"""
This question is asked by Apple. Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0

Ex: Given the following binary strings...

    "100" + "1", return "101"
    "11" + "1", return "100"
    "1" + "0", return  "1"
"""

# Time O(M) -> M being the len of the output string, which we are reversing
def get_binary_sum(b1, b2):
    carry = "0"
    pointer_1 = len(b1) - 1
    pointer_2 = len(b2) - 1

    output = ""

    while pointer_1 >= 0 and pointer_2 >= 0:
        carry, res_sum = sum_digits(b1[pointer_1], b2[pointer_2], carry)
        output += res_sum

        pointer_1 -= 1
        pointer_2 -= 1

    while pointer_1 >= 0:
        carry, res_sum = sum_digits(b1[pointer_1], carry, "0")
        output += res_sum

        pointer_1 -= 1
        
    while pointer_2 >= 0:
        carry, res_sum = sum_digits(b2[pointer_2], carry, "0")
        output += res_sum
    
        pointer_2 -= 1
    
    if carry != "0":
        output += carry
    return output[::-1]

def sum_digits(d1, d2, carry="0"):
    if d1 == "1" and d2 == "1":
        return ("1", "0") if carry=="0" else ("1", "1")
    elif d1 == "1" and d2 == "0" or d1 == "0" and d2 == "1":
        return ("0", "1") if carry=="0" else ("1", "0")
    return ("0", "0") if carry=="0" else ("0", "1")

print(get_binary_sum("100", "1"))
print(get_binary_sum("11", "1"))
print(get_binary_sum("1", "0"))
print(get_binary_sum("1000", "1000"))
print(get_binary_sum("1100", "1100"))