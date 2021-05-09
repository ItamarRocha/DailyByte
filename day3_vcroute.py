"""
This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

Ex: Given the following strings...

    "LR", return true
    "URURD", return false
    "RUULLDRD", return true
"""
# Solution 1

# Time O(n) n -> number of moves
# Space O(1)
def return_to_init(moves):
    init = (0,0)
    cur_coord = (0,0)
    for direction in moves:
        cur_coord = tuple(map(sum, zip(cur_coord, get_new_coord(direction))))
    return init == cur_coord

def get_new_coord(direction):
    if direction == "L":
        return (0, -1)
    elif direction == "R":
        return (0, 1)
    elif direction == "U":
        return (1, 0)
    elif direction == "D":
        return (-1, 0)
    return (0,0)

assert return_to_init("LR") == True
assert return_to_init("URURD") == False
assert return_to_init("RUULLDRD") == True

# Solution 2

def return_to_init2(moves):
    init = (0,0)
    cur_coord = (0,0)
    for direction in moves:
        cur_coord = get_new_coord2(direction, cur_coord)
    return init == cur_coord

def get_new_coord2(direction, cur_coord):
    change = None
    if direction == "L":
        change = (0, -1)
    elif direction == "R":
        change = (0, 1)
    elif direction == "U":
        change = (1, 0)
    elif direction == "D":
        change = (-1, 0)
    else:
        return cur_coord
    return (change[0] + cur_coord[0], change[1] + cur_coord[1])

assert return_to_init2("LR") == True
assert return_to_init2("URURD") == False
assert return_to_init2("RUULLDRD") == True