/*
This question is asked by Google. Given an NxM matrix, grid, where each cell in the matrix 
represents the cost of stepping on the current cell, return the minimum cost to traverse from
 the top-left hand corner of the matrix to the bottom-right hand corner.
Note: You may only move down or right while traversing the grid.

Ex: Given the following grid…

grid = [
    [1,1,3],
    [2,3,1],
    [4,6,1]
], return 7.
The path that minimizes our cost is 1->1->3->1->1 which sums to 7.
*/
#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

// Time O(n²)
// Space O(n²)
// class Solution{
// public:
//     int helper_minimize_path(vector<vector<int>> &grid, vector<vector<int>>& memo, int i, int j){
//         if(i >= grid.size() || j >= grid[0].size()) return INT_MAX;
//         else if(i == grid.size()-1 && j == grid[0].size()-1) return grid[i][j];
//         if(memo[i][j] != -1) return memo[i][j];

//         int right = helper_minimize_path(grid, memo, i, j+1);
//         int down = helper_minimize_path(grid, memo, i+1, j);

//         memo[i][j] = min(right, down) + grid[i][j];
//         return memo[i][j];
//     }
//     int minimize_path(vector<vector<int>> grid){
//         vector<vector<int>> memo(grid.size(), vector<int> (grid[0].size(), -1));
//         return helper_minimize_path(grid, memo, 0, 0);
//     }
// };
// Time O(n²)
// Space O(1)
class Solution{
public:
    int minimize_path(vector<vector<int>> grid){
        for(int i = 1; i < grid.size(); i++)
            grid[i][0] += grid[i-1][0];
        for(int j = 1; j < grid[0].size(); j++)
            grid[0][j] += grid[0][j-1];
        for(int i = 1; i < grid.size(); i++){
            for(int j = 1; j < grid[0].size(); j++){
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
            }
        }
        return grid[grid.size()-1][grid[0].size()-1];
    }
};
int main(){
    Solution s1 = Solution();
    cout << s1.minimize_path({{1,3,1},{1,5,1},{4,2,1}}) << endl;
    cout << s1.minimize_path({{1,2,3},{4,5,6}}) << endl;
    cout << s1.minimize_path({{7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5},{9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6},{8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8},{6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4},{7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4},{9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9},{1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4},{3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2},{1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3},{5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7},{2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7},{0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9}}) << endl;
}