"""
This question is asked by Amazon. A ship is about to set sail and you are responsible for its safety precautions. 
More specifically, you are responsible for determining how many life rafts to carry onboard. You are given a list
 of all the passengers’ weights and are informed that a single life raft has a maximum capacity of limit and can 
 hold at most two people. Return the minimum number of life rafts you must take onboard to ensure the safety of 
 all your passengers. Note: You may assume that a the maximum weight of any individual is at most limit.

Ex: Given the following passenger weights and limit…

weights = [1, 3, 5, 2] and limit = 5, return 3
weights = [1, 2] and limit = 3, return 1
weights = [4, 2, 3, 3] and limit = 5 return 3
"""
# Time O(nlogn)
# Space O(1)
def count_liferafts(weights, limit):
    weights.sort()

    cursor_1 = 0
    cursor_2 = len(weights) - 1

    life_rafts = 0
    
    current_count = 0

    added_one = True
    added_two = True

    while cursor_1 <= cursor_2:

        if current_count + weights[cursor_2] <= limit:
            current_count += weights[cursor_2]
            cursor_2 -= 1
            added_one = True
        else:
            added_one = False

        if current_count + weights[cursor_1] <= limit:
            current_count += weights[cursor_1]
            cursor_1 += 1
            added_two = True
        else:
            added_two = False

        if not added_one and not added_two:
            life_rafts += 1
            current_count = 0
    
    if current_count > 0:
        life_rafts += 1

    return life_rafts

print(count_liferafts([1, 3, 5, 2], 5)) # 3
print(count_liferafts([1, 2], 3)) # 1
print(count_liferafts([4, 2, 3, 3], 5)) # 3
print(count_liferafts([1,4,5,3,2], 5)) # 3
print(count_liferafts([1,2,3,5,5,5,4], 5)) # 5