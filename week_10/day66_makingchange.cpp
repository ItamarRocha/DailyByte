/*
This question is asked by Facebook. Given an array that represents different coin denominations and 
an amount of change you need to make, return the fewest number of coins it takes to make the given amount of change.
Note: If it is not possible to create the amount of change with the coins you’re given, return -1.

Ex: Given the following denominations and amount…

coins = [1,5, 10, 25], amount = 78, return 6
Take three 25 coins and three 1 coins for a total of 6 coins.
*/
#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;
// https://leetcode.com/problems/coin-change/solution/
// Time O(s * n) (s = amount , n is denomination coin)
// Space O(s)
// basically subtracts a coin at a time and uses the memo to store results
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if(amount < 1) return 0;
        vector<int> count(amount);
        return coinChange(coins, amount, count);
    }
private:
    int coinChange(vector<int>& coins, int rem, vector<int>& count){
        if(rem < 0) return -1;
        if(rem == 0) return 0;
        if(count[rem-1] != 0) return count[rem-1];
        int min = INT_MAX;
        for(auto coin: coins){
            int res = coinChange(coins, rem - coin, count);
            if(res >= 0 && res < min)
                min = 1 + res;
        }
        count[rem-1] = (min == INT_MAX)? -1: min;
        return count[rem-1];
    }
};

class Solution2 {
public:
    int coinChange2(vector<int>& coins, int amount) {
        if(amount < 1) return 0;
        vector<int> dp (amount+1,amount+1); // fill the array with the max, which is amount + 1
        dp[0] = 0;
        for(int j = 0; j < coins.size(); j++){
            for(int i = coins[j]; i<=amount; i++){
                dp[i] = min(dp[i], dp[i-coins[j]] + 1);
            }
        }
        // for(int i=0; i < dp.size(); i++){
        //     cout << dp[i] << " ";
        // }
        return dp[amount] <= amount? dp[amount]:-1;
    }
};

int main(){
    cout << "Solution 1" << endl;
    Solution s = Solution();
    vector<int> coins = {1,5,10,25};
    int amount = 78;
    cout << s.coinChange(coins, amount) << endl;

    coins = {1,2,3};
    amount = 7;
    cout << s.coinChange(coins, amount) << endl;

    coins = {80};
    amount = 78;
    cout << s.coinChange(coins, amount) << endl;

    coins = {1};
    amount = 0;
    cout << s.coinChange(coins, amount) << endl;

    coins = {2,5,10,1};
    amount = 27;
    cout << s.coinChange(coins, amount) << endl;

    cout << "\nSolution 2" << endl;
    Solution2 s2 = Solution2();
    coins = {1,5,10,25};
    amount = 78;
    cout << s2.coinChange2(coins, amount) << endl;

    coins = {1,2,3};
    amount = 7;
    cout << s2.coinChange2(coins, amount) << endl;

    coins = {80};
    amount = 78;
    cout << s2.coinChange2(coins, amount) << endl;

    coins = {1};
    amount = 0;
    cout << s2.coinChange2(coins, amount) << endl;

    coins = {2,5,10,1};
    amount = 27;
    cout << s2.coinChange2(coins, amount) << endl;
}