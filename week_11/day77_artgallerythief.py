"""
You’ve broken into an art gallery and want to maximize the value of the paintings you steal.
 All the paintings you steal you place in your bag which can hold at most W pounds. Given that 
 the weight and value of the ith painting is given by weights[i] and values[i] respectively, 
 return the maximum value you can steal.

Ex: Given the following W, weights array and values array…

W = 10, weights = [4, 1, 3], values = [4, 2, 7], return 13.

Ex: Given the following W, weights array and values array…

W = 5, weights = [2, 4, 3], values = [3, 7, 2], return 7.

Ex: Given the following W, weights array and values array…

W = 7, weights = [1, 3, 4], values = [3, 5, 6], return 11.
"""
#knapsack problem
"""
items/W    0   1   2   3   4   5
    0      0   0   0   0   0   0
    1      0   0   3   3   3   3
    2      0   0   3   3   7   7
    3      0   0   3   3   7   7

"""
# Time O(n²)
# Space O(n²)
def artgallerythief(W, weights, values):
    dp = [[0]* (W + 1) for _ in range(len(values) + 1)]

    for i in range(1, len(values) + 1):
        for j in range(1, W+1):
            dp[i][j] = dp[i-1][j]
            if j >= weights[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
            
    return dp[-1][-1]

print(artgallerythief(10, [4,1,3], [4,2,7]))


print(artgallerythief(5, [2,4,3], [3,7,2]))


print(artgallerythief(7, [1,3,4], [3,5,6]))