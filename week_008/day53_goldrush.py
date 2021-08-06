"""
This question is asked by Amazon. Given a 2D matrix that represents a gold mine, where each cell’s 
value represents an amount of gold, return the maximum amount of gold you can collect given the following rules:

You may start and stop collecting gold from any position
You can never visit a cell that contains 0 gold
You cannot visit the same cell more than once
From the current cell, you may walk one cell to the left, right, up, or down
Ex: Given the following gold mine…

goldMine = [
    [0,2,0],
    [8,6,3],
    [0,9,0]
],
return 23 (start at 9 and then move to 6 and 8 respectively)
"""
# Time O((n*m)²)
# Space O(n*m) # we are not using more than the space given by goldmine, but we are using the call stack

def goldrush(goldmine):
    max_gold = 0

    for i in range(len(goldmine)):
        for j in range(len(goldmine[0])):
            if goldmine[i][j] == 0:
                continue
            res = search(goldmine, i, j)
            max_gold = max(res, max_gold)
    return max_gold
            
    
            
def search(goldmine, i, j):
    if i < 0 or j < 0 or i >= len(goldmine) or j >= len(goldmine[0]) or goldmine[i][j] == 0:
        return 0

    goldmine[i][j], temp = 0, goldmine[i][j] #same as using a set

    s = [0] * 4
    s[0] = search(goldmine, i+1, j)
    s[1] = search(goldmine, i, j+1)
    s[2] = search(goldmine, i-1, j)
    s[3] = search(goldmine, i, j-1)
    
    goldmine[i][j] = temp

    return  max(s) + goldmine[i][j]

goldmine = [[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]


print(goldrush(goldmine))