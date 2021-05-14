# Time O(n) n -> number of characters in str1
# Space O(n) [this happens because we are creating a list
#             out of our string, since python strings are
#             immutable]
def reverse_string(str1):
    str1 = list(str1)

    i = 0
    j = len(str1) - 1
    
    while i <= j:
        str1[i], str1[j] = str1[j], str1[i]
        i += 1
        j -= 1
    
    return "".join(str1)

# Works better, since we dont need to create a list, and 
# use a visible loop here.
def reverse_string2(str1):
    return str1[::-1]

assert reverse_string("The Daily Byte") == "etyB yliaD ehT"
assert reverse_string("Cat") == "taC"
assert reverse_string("civic") == "civic"

print("yey all done")

assert reverse_string2("The Daily Byte") == "etyB yliaD ehT"
assert reverse_string2("Cat") == "taC"
assert reverse_string2("civic") == "civic"

print("2nd function done")