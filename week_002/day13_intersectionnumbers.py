"""
This question is asked by Google. Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

    nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
    nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
    nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
"""

# Time O(m + n)
# Space O(m)
def get_intersection(nums1, nums2):
    array_set = set(nums1)

    output = []

    for el in nums2:
        if el in array_set:
            output.append(el)
            array_set.remove(el)
        
    return output

print(get_intersection([2, 4, 4, 2], [2,4]))
print(get_intersection([1, 2, 3, 3], [3,3]))
print(get_intersection([2, 4, 6, 8], [1,3,5,7]))