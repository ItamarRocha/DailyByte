"""
This question is asked by Google. You are given a bag of coins, an initial energy of E, and want
 to maximize your number of points (which starts at zero). To gain a single point you can exchange 
 coins[i] amount of energy (i.e. if I have 100 energy and a coin that has a value 50 I can exchange
  50 energy to gain a point). If you do not have enough energy you can give away a point in exchange
   for an increase in energy by coins[i] amount (i.e. you give away a point and your energy is increased
    by the value of that coin: energy += coins[i]). Return the maximum number of points you can gain.
Note: Each coin may only be used once.

Ex: Given the following coins and starting energy…

coins = [100, 150, 200] and E = 150, return 1
coins = [100,200,300,400] and E = 200, return 2
coins = [300] and E = 200, return 0
"""
# Time O(nlogn)
# Space O(n) só o array fornecido
def maxcoins(coins, E):
    coins.sort()
    l,r = 0, len(coins)-1

    points = 0
    answer = 0
    while l <= r:
        if E >= coins[l]:
            E -= coins[l]
            points += 1
            l += 1
        elif points > 0:
            E += coins[r]
            points -= 1
            r -= 1
        else:
            break
        answer = max(answer, points)
    return answer

print(maxcoins([100,150,200], 150)) # 1
print(maxcoins([100,200,300,400], 200)) # 2
print(maxcoins([300], 200)) # 0