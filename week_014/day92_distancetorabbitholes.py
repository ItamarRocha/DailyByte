"""
Given a 2D array containing only the following values: -1, 0, 1 where -1 represents an obstacle, 0 represents a rabbit hole, and 1 represents a rabbit,
 update every cell containing a rabbit with the distance to its closest rabbit hole.

Note: multiple rabbit may occupy a single rabbit hole and you may assume every rabbit can reach a rabbit hole. 
A rabbit can only move up, down, left, or right in a single move. Ex: Given the following grid…

-1  0  1
 1  1 -1
 1  1  0
your grid should look like the following after running the function...
-1  0  1
2  1 -1
2  1  0

Ex: Given the following grid…

 1  1  1
 1 -1 -1
 1  1  0
your grid should look like the following after running the function...
4  5  6
3 -1 -1
2  1  0
"""
def distancetorabbitholes(grid):
    # memo = [[0] * len(grid[0]) for _ in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # print(f"i = {i}, j = {j}")
            if grid[i][j] == 1 or grid[i][j] == float("inf"):
                # print(i,j, grid)
                dfs(grid, i, j)
                # print(grid)
    
    return grid

def dfs(grid, i, j):
    # print(i,j)

    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or grid[i][j] == -1:
        return float("inf")

    if grid[i][j] == 0:
        return 0
    elif grid[i][j] != 1 and grid[i][j] != float("inf"):
        return grid[i][j]

    grid[i][j] = -1 # keep track of what was visited
    
    d = dfs(grid, i+1, j)
    u = dfs(grid, i-1, j)
    r = dfs(grid, i, j+1)
    l = dfs(grid, i, j-1)
    
    grid[i][j] = 1 + min(l,r,u,d)
    return grid[i][j]

print(distancetorabbitholes([[1,1,1],
 [1,-1,-1],
 [1,1,0]]))

print(distancetorabbitholes([[-1,0,1],
 [1,1,-1],
 [1,1,0]]))