"""
This question is asked by Facebook. Given an integer array, return the sum of its contiguous subarray that produces the largest value.
Note: Your subarray must contain at least one value.

Ex: Given the following integer arrays…

nums = [-3,8,-8,2], return 8 (8)
nums = [2, 3,-4, 2], return 5 (2 + 3)
nums = [1, 5,-2, -3, 7], return 8 (1 + 5 + (-2) + (-3) + 7)
"""
# Time O(n²)
# Space O(1)
def maximumsubarray(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i,len(nums)):
            # print(j, cur_sum)
            cur_sum += nums[j]
            max_sum = max(max_sum, cur_sum)
    return max_sum

print(maximumsubarray([-3,8,-8,2])) # 8
print(maximumsubarray([2, 3,-4, 2])) # 5
print(maximumsubarray([1, 5,-2, -3, 7])) # 8

# Time O(n)
# Space O(1)
def maximumsubarray(nums):
    max_sum = nums[0]
    cur_sum = nums[0]
    for i in range(1,len(nums)):
        cur_sum = max(cur_sum + nums[i], nums[i])
        max_sum = max(cur_sum, max_sum)

    return max_sum

print(maximumsubarray([-3,8,-8,2])) # 8
print(maximumsubarray([2, 3,-4, 2])) # 5
print(maximumsubarray([1, 5,-2, -3, 7])) # 8