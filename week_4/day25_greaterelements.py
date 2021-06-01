"""
This question is asked by Amazon. Given two arrays of numbers, where the first array is a subset of the second array, return an array containing all the next 
greater elements for each element in the first array, in the second array. If there is no greater element for any element, output -1 for that number.

Ex: Given the following arrays…

    nums1 = [4,1,2], nums2 = [1,3,4,2], return [-1, 3, -1] because no element in nums2 is greater than 4, 3 is the first number in nums2 greater than 1, and no element in nums2 is greater than 2.
    nums1 = [2,4], nums2 = [1,2,3,4], return [3, -1] because 3 is the first greater element that occurs in nums2 after 2 and no element is greater than 4.
"""
# Time O(n)
# Space O(n)
def greater_elements(subset, array):
    result = {}
    stack = []
    # print(array)
    for idx in range(len(array)):
        # print("current idx = ", idx)
        # print("stack = ", stack)
        # print("result = ", result, "\n")
        while stack and array[stack[-1]] < array[idx]:
            top = stack.pop()
            result[array[top]] = array[idx]
            
        stack.append(idx)

    output = []
    for el in subset:
        if el in result:
            output.append(result[el])
        else:
            output.append(-1)
    return output

print(greater_elements([4,1,2], [1,3,4,2]))
print(greater_elements([2,4],[1,2,3,4]))