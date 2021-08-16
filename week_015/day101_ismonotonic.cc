/*
This question is asked by Facebook. Given an array nums, return whether or not its values are monotonically increasing or monotonically decreasing.
Note: An array is monotonically increasing if for all values i <= j, nums[i] <= nums[j]. Similarly an array is monotonically decreasing if for all values i <= j, nums[i] >= nums[j].

Ex: Given the following array nums…

nums = [1, 2, 3, 4, 4, 5], return true.
Ex: Given the following array nums…

nums = [7, 6, 3], return true.
Ex: Given the following array nums…

nums = [8, 4, 6], return false.
*/
#include <iostream>
#include <vector>

// bool monotonically(std::vector<int> nums){
//     bool is_monotonically = true;
//     int last_el = nums[0];

//     for(int i = 1; i < nums.size(); i++){
//         if(nums[i] < last_el){
//             is_monotonically = false;
//             break;
//         }
//         last_el = nums[i];
//     }
//     if(is_monotonically)
//         return true;
//     is_monotonically = true;
//     last_el = nums[0];
//     for(int i = 1; i < nums.size(); i++){
//         if(nums[i] > last_el){
//             is_monotonically = false;
//             break;
//         }
//         last_el = nums[i];
//     }
//     return is_monotonically;
// }

bool monotonically(std::vector<int> nums){
    bool is_monotonically_incr = true;
    bool is_monotonically_decr = true;
    int last_el = nums[0];

    for(int i = 1; i < nums.size(); i++){
        if(nums[i] > last_el){
            is_monotonically_incr = false;
        }
        if(nums[i] < last_el){
            is_monotonically_decr = false;
        }
        last_el = nums[i];
        if(!(is_monotonically_incr || is_monotonically_decr))
            break;
    }
    return is_monotonically_incr || is_monotonically_decr;
}

int main(){
    std::cout << monotonically({1,2,3,4,4,5}) << std::endl;
    std::cout << monotonically({7,6,4}) << std::endl;
    std::cout << monotonically({8,4,6}) << std::endl;
}