"""
You are transporting bricks on a construction site and want to work as efficiently as possible.
 The weight of each brick is given by bricks[i]. Given a wheelbarrow that can carry up to (not including)
  5000 pounds, return then maximum number of bricks you can place in your wheelbarrow to transport.

Ex: Given the following bricks…

bricks = [1000, 1000, 1000, 2000], return 3.

Ex: Given the following bricks…

bricks = [1000, 200, 150, 200], return 4.
"""
# Time O(nlogn)
# Space O(1)
def moving_bricks(bricks):
    bricks.sort()

    total_sum = 0
    counter = 0
    i = 0

    while i < len(bricks):
        if total_sum + bricks[i] >= 5000:
            return counter
        
        total_sum += bricks[i]
        counter += 1
        i+=1
    
    return counter

print(moving_bricks([1000, 1000, 1000, 2000]))
print(moving_bricks([1000, 200, 150, 200]))