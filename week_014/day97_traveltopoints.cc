/*
This question is asked by Facebook. Given N points on a Cartesian plane, return the minimum time required to visit all points in the order that they’re given.
Note: You start at the first point and can move one unit vertically, horizontally, or diagonally in a single second.

Ex: Given the following points…

points = [[0, 0], [1,1], [2,2]], return 2.
In one second we can travel from [0, 0] to [1, 1]
In another second we can travel from [1, 1,] to [2, 2]
Ex: Given the following points…

points = [[0, 1], [2, 3], [4, 0]], return 5.
*/
#include <iostream>
#include <vector>

using namespace std;

// Time O(n)
// space O(1)
int traveltopoints(vector<vector<int>> points){
    int total_distance = 0;
    pair<int,int> diff;
    for(int i = 1; i < points.size(); i++){
        diff.first = abs(points[i][0] - points[i-1][0]);
        diff.second = abs(points[i][1] - points[i-1][1]);
        // cout << diff.first << " " << diff.second << endl;
        total_distance += max(diff.first, diff.second);  
    }
    return total_distance;
}

int main(){
    cout << traveltopoints({{0,1},{2,3},{4,0}}) << endl; // 2
    cout << traveltopoints({{0,0},{1,1},{2,2}}) << endl; // 5
    cout << traveltopoints({{1,1},{3,4},{-1,0}}) << endl; // 7
    cout << traveltopoints({{3,2},{-2,2}}) << endl; // 5
}