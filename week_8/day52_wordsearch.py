"""
This question is asked by Amazon. Given a 2D board that represents a word search puzzle and a string word, 
return whether or the given word can be formed in the puzzle by only connecting cells horizontally and vertically.

Ex: Given the following board and words…

board =
[
  ['C','A','T','F'],
  ['B','G','E','S'],
  ['I','T','A','E']
]
word = "CAT", return true
word = "TEA", return true
word = "SEAT", return true
word = "BAT", return false
"""
def search_word(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            seen = set()
            if search(board, i, j, seen, word):
                return True
        
    return False

def search(board, i, j, seen, word):
    if len(word) == 0:
        return True

    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or \
        board[i][j] != word[0] or (i,j) in seen:
        return False

    seen.add((i,j))

    s1 = search(board, i+1, j, seen, word[1:])
    s2 = search(board, i, j+1, seen, word[1:])
    s3 = search(board, i-1, j, seen, word[1:])
    s4 = search(board, i, j-1, seen, word[1:])

    if s1 or s2 or s3 or s4:
        return True
    seen.remove((i,j))
    return False

print(search_word([["A","B","C","E"],
                    ["S","F","E","S"],
                    ["A","D","E","E"]], "ABCESEEEFS"))


print(search_word([['C','A','T','F'],
                    ['B','G','E','S'],
                    ['I','T','A','E']], "CAT"))

print(search_word([['C','A','T','F'],
                    ['B','G','E','S'],
                    ['I','T','A','E']], "TEA"))

print(search_word([['C','A','T','F'],
                    ['B','G','E','S'],
                    ['I','T','A','E']], "SEAT"))

print(search_word([['C','A','T','F'],
                    ['B','G','E','S'],
                    ['I','T','A','E']], "BAT"))