"""
This question is asked by Apple. Given a staircase where the ith step has a non-negative
 cost associated with it given by cost[i], return the minimum cost of climbing to the top 
 of the staircase. You may climb one or two steps at a time and you may start climbing from 
 either the first or second step.

Ex: Given the following cost array…

cost = [5, 10, 20], return 10.

Ex: Given the following cost array…

cost = [1, 5, 10, 3, 7, 2], return 10.
"""
# Time O(n)
# Space O(n)
def climbing_stairs(costs):
    cumulative_costs = [0] * len(costs)
    cumulative_costs[0], cumulative_costs[1] = costs[0], costs[1]

    for i in range(2, len(costs)):
        cumulative_costs[i] = costs[i] + min(cumulative_costs[i-1], cumulative_costs[i-2])

    return min(cumulative_costs[len(costs)-1], cumulative_costs[len(costs)-2])

print(climbing_stairs([5,10,20]))
print(climbing_stairs([1,5,10,3,7,2]))
print(climbing_stairs([10,15,20]))
print(climbing_stairs([1,100,1,1,1,100,1,1,100,1]))

# Time O(n)
# Space O(1)
def climbing_stairs(costs):
    last_2, last_1 = costs[0], costs[1]
    for i in range(2, len(costs)):
        last_1, last_2 = costs[i] + min(last_1, last_2), last_1

    return min(last_1, last_2)

print(climbing_stairs([5,10,20]))
print(climbing_stairs([1,5,10,3,7,2]))
print(climbing_stairs([10,15,20]))
print(climbing_stairs([1,100,1,1,1,100,1,1,100,1]))