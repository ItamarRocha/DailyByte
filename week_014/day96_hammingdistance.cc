/*
This question is asked by Facebook. Given two integers x and y, return the hamming distance between the two numbers.
Note: The hamming distance between two numbers is the number of bit positions in which the bits differ.

Ex: Given the following integers x and y…

x = 2, y = 4, return 2.
2 in binary is 0 0 1 0
4 in binary is 0 1 0 0
therefore the number of positions in which the bits differ is two.
*/
#include <iostream>
#include <bitset>
#include <algorithm>

using namespace std;

// Time O(1) # we could say O(32)
// Space O(1) # we could say O(64) cause we are storing 64 bits;
int hamming_distance(int x, int y){
    int const max_size = 32;
    string bin_x = bitset<max_size>(x).to_string();
    string bin_y = bitset<max_size>(y).to_string();

    int distance = 0;

    for(int i = max_size - 1; i >= 0; i--){
        if(bin_x[i] != bin_y[i])
            distance += 1;
    }

    return distance;
}
// Space can be just O(32) here :P
int hamming_distance2(int x, int y){
    string z = bitset<32>(x^y).to_string(); // we just have to sum the bits now to see how many different ones we have
    return count(z.begin(), z.end(), '1');
}
int main(){
    cout << hamming_distance2(2,4) << endl;
}