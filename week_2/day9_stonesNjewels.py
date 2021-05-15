"""
This question is asked by Amazon. Given a string representing your stones and another string representing a list of jewels, return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

    jewels = "abc", stones = "ac", return 2
    jewels = "Af", stones = "AaaddfFf", return 3
    jewels = "AYOPD", stones = "ayopd", return 0
"""

# Time O(n + m) n -> number of jewels m -> number of stones
# Space O(n)
def jewelsstones(jewels, stones):
    jewels_set = set()

    for el in jewels:
        jewels_set.add(el)

    jewels_count = 0

    for el in stones:
        if el in jewels_set:
            jewels_count += 1

    return jewels_count

print(jewelsstones("abc", "ac"))
print(jewelsstones("Af", "AaaddfFf"))
print(jewelsstones("AYOPD", "aayopd"))