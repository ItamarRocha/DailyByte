"""
This question is asked by Apple. Given a list of positive numbers without duplicates and 
a target number, find all unique combinations of the numbers that sum to the target. 
Note: You may use the same number more than once.

Ex: Given the following numbers and target…

numbers = [2,4,6,3], target = 6,
return [
    [2,2,2],
    [2,4],
    [3,3],
    [6]
]
"""
# Time O(n^t) t = target
# Space O(n)
def unique_combinations(numbers, target):
    output = []
    combinations_generator(numbers,target,output)
    return output

def combinations_generator(numbers, target, output, cur_sequence=[]):
    if target < 0:
        return
    if target == 0:
        output.append(cur_sequence[:])
        return output
    
    for i in range(len(numbers)):
        el = numbers[i]
        combinations_generator(numbers[i:], target - el, output, cur_sequence + [el])

    return output

print(unique_combinations([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(unique_combinations([2,4,6,3], 6))
print(unique_combinations([2], 1))
print(unique_combinations([1], 1))
print(unique_combinations([1], 2))