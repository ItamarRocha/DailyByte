"""
This question is asked by Facebook. Given a character array, compress it in place and return the new length of the array.
Note: You should only compress the array if its compressed form will be at least as short as the length of its original form.

Ex: Given the following character array chars…

chars = ['a', 'a', 'a', 'a', 'a', 'a'], return 2.
chars should be compressed to look like the following:
chars = ['a', '6']
Ex: Given the following character array chars…

chars = ['a', 'a', 'b', 'b', 'c', 'c'], return 6.
chars should be compressed to look like the following:
chars = ['a', '2', 'b', '2', 'c', '2']
Ex: Given the following character array chars…

chars = ['a', 'b', 'c'], return 3.
In this case we chose not to compress chars.
https://leetcode.com/problems/string-compression/
"""
# doing it without inplace
def compression(chars):
    counter = 1
    output = [chars[0]]

    for i in range(1, len(chars)):
        if chars[i] == output[-1]:
            counter += 1
        else:
            for c in str(counter):
                output.append(c)
            output.append(chars[i])
            counter = 1
    for c in str(counter):
        output.append(c)
    
    return len(output) if len(output) < len(chars) else len(chars)

# print(compression(["a","b","c"]))
# print(compression(['a', 'a', 'b', 'b', 'c', 'c']))
# print(compression(['a', 'a', 'a', 'a', 'a', 'a']))
# print(compression(['a', 'a', 'b', 'b', 'c', 'c',"c"]))

# doing it inplace
# Time O(n + k)
# Space O(1)
def compression(chars):
    counter = 1

    array_cursor = 1 # where we will insert
    cursor = 0 # the number we are current on
    i = 1

    while i < len(chars):
        while i < len(chars) and chars[i] == chars[cursor]:
            i+=1
            counter += 1
        if counter != 1:
            for c in str(counter):
                cursor += 1
                chars[cursor] = c
        
        if i >= len(chars):
            break
        cursor += 1
        chars[cursor] = chars[i]
        counter = 1
        i+=1
        
    return len(chars[:cursor+1])

print(compression(["a","b","c"]))
print(compression(['a', 'a', 'b', 'b', 'c', 'c']))
print(compression(['a', 'a', 'a', 'a', 'a', 'a']))
print(compression(['a', 'a', 'b', 'b', 'c', 'c',"c"]))