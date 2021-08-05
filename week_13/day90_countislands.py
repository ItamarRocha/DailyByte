"""
Given a 2D array of integers with ones representing land and zeroes representing water, 
return the number of islands in the grid. Note: an island is one or more ones surrounded 
by water connected either vertically or horizontally. Ex: Given the following grid…

11000
11010
11001
return 3.
Ex: Given the following grid…

00100
00010
00001
00001
00010
return 4.
"""
# Time O(n²)
# Space O(n²) (with recursion and a set)
def count_islands(grid):
    seen = set()
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0 or (i,j) in seen:
                continue
            
            dfs(grid, i, j, seen)
            counter += 1
    
    return counter

def dfs(grid, i ,j, seen):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 
    
    if (i,j) in seen or grid[i][j] == 0:
        return

    seen.add((i,j))

    dfs(grid, i+1, j, seen)
    dfs(grid, i-1, j, seen)
    dfs(grid, i, j+1, seen)
    dfs(grid, i, j-1, seen)

    return

grid = [[1,1,0,0,0],
        [1,1,0,1,0],
        [1,1,0,0,1]]

print(count_islands(grid))

grid = [[0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,1,0]]

print(count_islands(grid))

# Time O(n²)
# Space O(n²) (with recursion only)
def count_islands(grid):
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                continue
            
            dfs(grid, i, j)
            counter += 1
    
    return counter

def dfs(grid, i ,j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 
    
    if grid[i][j] == 0:
        return

    grid[i][j] = 0

    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

    return

grid = [[1,1,0,0,0],
        [1,1,0,1,0],
        [1,1,0,0,1]]

print(count_islands(grid))

grid = [[0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,1,0]]

print(count_islands(grid))

# we can also do it with bfs, but dfs is cleaner :P
# Okay, lets do it with BFS '-'

def count_islands(grid):
    counter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                continue
        
            bfs(grid, i, j)
            counter+=1
            
    return counter

def bfs(grid, i, j):
    queue = [(i,j)]

    while queue:

        x,y = queue.pop(0)
        
        if grid[x][y] == 0:
            continue
        
        grid[x][y] = 0

        if (x - 1) >= 0 and grid[x-1][y] == 1:
            queue.append((x-1,y))
        if (y - 1) >= 0 and grid[x][y-1] == 1:
            queue.append((x,y -1))
        if (x + 1) < len(grid) and grid[x+1][y] == 1:
            queue.append((x+1,y))
        if (y + 1) < len(grid[0]) and grid[x][y+1] == 1:
            queue.append((x,y + 1))
    
    return

grid = [[1,1,0,0,0],
        [1,1,0,1,0],
        [1,1,0,0,1]]

print(count_islands(grid))

grid = [[0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,1,0]]

print(count_islands(grid))