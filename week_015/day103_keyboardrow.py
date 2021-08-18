# Given a list of words, return all the words that require only a single row of a keyboard to type.
# Note: You may assume that all words only contain lowercase alphabetical characters.

# Ex: Given the following list of words…

# words = ["two", "dad", "cat"], return ["two", "dad"].
# Ex: Given the following list of words…

# words = ["ufo", "xzy", "byte"], return [].

# will do it one day in c++
# Time O(n * l) n-> words , l ->length
# Space O(n)
rows = [[set()], [set()],[set()]]
def twokeyboardrow(words):
    output = []

    for word in words:
        row_count = set()
        for chr in word:
            for i in range(len(rows)):
                if chr in rows[i]:
                    row_count.add(i)
        
        if len(row_count) == 1:
            output.append(word)

    return output