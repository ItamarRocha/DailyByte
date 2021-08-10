/*
This question is asked by Amazon. Given a string s remove all the vowels it contains and return the resulting string.
Note: In this problem y is not considered a vowel.

Ex: Given the following string s…

s = "aeiou", return ""
Ex: Given the following string s…

s = "byte", return "byt"
Ex: Given the following string s…

s = "xyz", return "xyz"
*/
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

string removing_vowels(string str){
    unordered_set <char> set = {'a', 'e', 'i', 'o', 'u'};
    string output;
    // cout << str.length() << endl;
    for(int i=0; i < str.length(); i++){
        if(!set.count(str[i])){
            output.push_back(str[i]);
        }
    }
    return output;
}

int main(){       
    // Test 1
    string str = "aeiou";
    string output = removing_vowels(str);
    
    for(auto el: output){
        cout << el;
    }
    cout << endl;

    // Test 2
    string str2 = "byte";
    string output2 = removing_vowels(str2);
    
    for(auto el: output2){
        cout << el;
    }
    cout << endl;

    // Test 3
    string str3 = "xyz";
    string output3 = removing_vowels(str3);
    
    for(auto el: output3){
        cout << el;
    }
    cout << endl;
}