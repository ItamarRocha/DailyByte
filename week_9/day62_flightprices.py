"""
This question is asked by Google. A company is booking flights to send its employees to its two satellite
 offices A and B. The cost of sending the ith employee to office A and office B is given by prices[i][0] and prices[i][1]
  respectively. Given that half the employees must be sent to office A and half the employees must be sent to office B,
   return the minimum cost the company must pay for all their employees’ flights.

Ex: Give the following prices…

prices = [[40,30],[300,200],[50,50],[30,60]], return 310
Fly the first personn to office B.
Fly the second person to office B.
Fly the third person to office A.
Fly the fourth person to office A.
"""
# Time O(n!), which will give us time limit exceeded
# Space O(n)
def flight_prices(prices):
    return prices_helper(prices, len(prices)//2, len(prices)//2, set())

def prices_helper(prices, c1, c2, seen=set()):
    # print(c1, c2)
    if c1 == 0 and c2 == 0:
        return 0
    min_value = float("inf")
    for i in range(len(prices)):
        if i not in seen:
            seen.add(i)
            if c1:
                min_value = min(min_value, prices[i][0] + prices_helper(prices, c1 - 1, c2, seen))
            if c2:
                min_value = min(min_value, prices[i][1] + prices_helper(prices, c1, c2 - 1, seen))
            seen.remove(i)
    # print(min_value)
    return min_value

print(flight_prices([[40,30],[300,200],[50,50],[30,60]]))

# Time O(2^n) which will also give us time limit exceed
# Space O(n)
def flight_prices(prices):
    return prices_helper(prices, 0, len(prices)//2, len(prices)//2)

def prices_helper(prices, cursor, c1, c2):
    # print(c1, c2)
    if c1 == 0 and c2 == 0:
        return 0
    min_value = float("inf")
        
    if c1:
        min_value = min(min_value, prices[cursor][0] + prices_helper(prices, cursor+1, c1 - 1, c2))
    if c2:
        min_value = min(min_value, prices[cursor][1] + prices_helper(prices, cursor+1, c1, c2 - 1))
    
    return min_value

print(flight_prices([[40,30],[300,200],[50,50],[30,60]]))


# Time O(n²)
# Space O(n²)
def flight_prices(prices):
    memo = {}
    return prices_helper(prices, 0, len(prices)//2, len(prices)//2, memo)

def prices_helper(prices, cursor, c1, c2, memo):
    if (c1, c2) in memo:
        return memo[(c1, c2)]
    if c1 == 0 and c2 == 0:
        return 0
    min_value = float("inf")
        
    if c1:
        min_value = min(min_value, prices[cursor][0] + prices_helper(prices, cursor+1, c1 - 1, c2, memo))
    if c2:
        min_value = min(min_value, prices[cursor][1] + prices_helper(prices, cursor+1, c1, c2 - 1, memo))
    
    # print(cursor, c1, c2, min_value)
    memo[(c1, c2)] = min_value
    return min_value

print(flight_prices([[40,30],[300,200],[50,50],[30,60]]))

# Time O(nlogn)
# Space O(n)
# we put everyone in city 1 and then subtract the smallest diffs to city 2
def flight_prices(prices):
    total_first_city_sum = sum(price[0] for price in prices)
    diff = [price[1] - price[0] for price in prices]
    diff.sort()
    return total_first_city_sum + sum(diff[:len(diff)//2])

print(flight_prices([[40,30],[300,200],[50,50],[30,60]]))

# Time O(nlogn)
# Space O(n)
# get the diffs and sort em
def flight_prices(prices):
    diff = sorted(prices, key= lambda x: x[1]-x[0]) # more negative, better to be city 2
    return sum(x[1] for x in diff[:len(diff)//2]) + sum(x[0] for x in diff[len(diff)//2:])

print(flight_prices([[40,30],[300,200],[50,50],[30,60]]))
