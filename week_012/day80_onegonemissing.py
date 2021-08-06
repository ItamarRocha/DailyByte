"""
This question is asked by Amazon. Given an array that contains all distinct values from
 zero through N except one number, return the number that is missing from the array.

Ex: Given the following array nums…

nums = [1, 4, 2, 0], return 3.
3 is the only number missing in the array between 0 and 4.
Ex: Given the following array nums…

nums = [6, 3, 1, 2, 0, 5], return 4.
4 is the only number missing in the array between 0 and 6.
"""
# Time O(n)
# Space O(1)
def onegonemissing(nums):
    n = len(nums)
    total_sum = (n * (n+1))//2
    return total_sum - sum(nums)

print(onegonemissing([1,4,2,0]))
print(onegonemissing([6,3,1,2,0,5]))