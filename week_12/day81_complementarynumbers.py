"""
Given a positive number, return its complementary number.
Note: The complement of a number is the number that results from flipping every bit in the original
 number. (i.e. zero bits become one bits and one bits become zero bits).

Ex: Given the following number…

number = 27, return 4.
27 in binary (not zero extended) is 11011.
Therefore, the complementary binary is 00100 which is 4.
"""

# Time O(n)
def complementary(n):
    bin_n = bin(n)[2:]
    new_n = ""

    for el in bin_n:
        new_n += "0" if el == "1" else "1"

    return int(new_n, base=2)

print(complementary(27))

def complementary(n):
    mask = 1 << len(bin(n)[2:])
    print(mask)
    return (mask - 1) ^ n

print(complementary(27))