/*
This question is asked by Amazon. Given an array of integers, nums, sort the array in any manner such that when i is even, nums[i] is even and when i is odd, nums[i] is odd.
Note: It is guaranteed that a valid sorting of nums exists.

Ex: Given the following array nums…

nums = [1, 2, 3, 4], one possible way to sort the array is [2,1,4,3]
https://leetcode.com/problems/sort-array-by-parity-ii/
*/

#include <iostream>
#include <vector>

using namespace std;
// Time O(n)
// Space O(1)
vector<int> sortArrayByParity(vector<int>& nums) {
    int even_cursor = 0, odd_cursor = 1;

    while(even_cursor < nums.size() && odd_cursor < nums.size()){
        if(nums[even_cursor] % 2 == 0){
            even_cursor += 2;
        }else if(nums[odd_cursor] % 2 == 1){
            odd_cursor += 2;
        }else{
            swap(nums[odd_cursor], nums[even_cursor]);
            odd_cursor += 2;
            even_cursor += 2;
        }
    }
    return nums;
}

int main(){
    vector<int> nums = {4,2,5,7};
    vector<int> res = sortArrayByParity(nums);
    for(auto el: res)
        cout << el << " ";
}