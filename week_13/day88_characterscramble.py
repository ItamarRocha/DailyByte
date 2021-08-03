"""
This question is asked by Amazon. Given two strings, passage and text return whether or not the characters in text can be used to form the given passage.
Note: Each character in text may only be used once and passage and text will only contain lowercase alphabetical characters.

Ex: Given the following passage and text…

passage = "bat", text = "cat", return false.
Ex: Given the following passage and text…

passage = "dog" text = "didnotgo", return true.
"""
# Time O(t + p)
# Space O(t)
def character_scramble(passage, text):
    char_count = {}
    for el in text:
        if el not in char_count:
            char_count[el] = 1
        else:
            char_count[el] += 1

    for el in passage:
        if el not in char_count or char_count[el] - 1 < 0:
            return False
        char_count[el] -= 1
    
    return True

print(character_scramble("bat", "cat"))
print(character_scramble("dog", "didnotgo"))