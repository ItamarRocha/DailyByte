/*
https://leetcode.com/problems/move-zeroes
This question is asked by Apple. Given an array of numbers, move all zeroes in the array to the end while maintaining the relative order of the other numbers.
Note: You must modify the array you’re given (i.e. you cannot create a new array).

Ex: Given the following array nums…

nums = [3, 7, 0, 5, 0, 2], rearrange nums to look like the following [3,7,5,2,0,0]
*/
#include <iostream>
#include <vector>

using namespace std;
// Time O(n)
vector<int> rearrange(vector<int> arr){
    int last_zero = 0;

    for(int i = 0; i < arr.size(); i++){
        if(arr[i] != 0 && arr[last_zero] == 0){
            swap(arr[i], arr[last_zero]);
            last_zero += 1;
        }else if(arr[last_zero] != 0){
            last_zero += 1;
        }
    }

    for(auto el:arr){
        cout << el << " ";
    }
    return arr;
}

int main(){
    rearrange({3,7,0,5,0,2});
}