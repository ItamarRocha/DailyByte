/*
This question is asked by Microsoft. Given a message that is encoded using the following encryption method…

A -> 1
B -> 2
C -> 3
...
Z -> 26
Return the total number of ways it can be decoded.
Note: ‘0’ has no mapping and a character following a ‘0’ also has no mapping (i.e. “03”)


Ex: Given the following message…

message = "23", return 2.
The message can be decrypted as "BC" (i.e. 2 -> B, 3 -> C)
The message can also be decrypted as "W" (i.e. 23 -> W)
Ex: Given the following message…

message = "1234", return 3.
*/
#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;
// Time O(n)
// Time O(n)
int helperDecodings(string s, int i, map<int,int>& memo);

int numDecodings(string s){
    map<int,int> memo;
    return helperDecodings(s, 0, memo);
}
bool is_valid(string sub_s){
    // cout << sub_s << endl;
    if(sub_s[0] == '0'){
        return false;
    }
    int converted = (stoi(sub_s));
    if(converted <= 26 && converted >= 1)
        return true;
    return false;
}

int helperDecodings(string s, int i, map<int,int>& memo){
    // cout << s << " "<< s.size() <<" "<< i << endl;
    if(i == s.size()){
        return 1;
    }else if(i > s.size()){
        return 0;
    }

    if(memo.find(i) != memo.end()){
        return memo[i];
    }

    int count = 0;
    // cout << s.substr(i,1) << " i = " << i <<" " <<s.substr(i,2) << endl;
    if(is_valid(s.substr(i,1)))
        count += helperDecodings(s, i+1, memo);
    if(i+1 < s.size() && is_valid(s.substr(i,2)))
        count += helperDecodings(s, i+2, memo);

    memo[i] = count;
    return count;
}
int num(int i, string &s, vector<int> &mem);
// como a gente tem um memo do tamanho da string dava pra ter usado só um vetor mesmo.
int numDecodings2(string s) {
    int n = s.size();
    vector<int> mem(n+1,-1);
    mem[n]=1;
    return s.empty()? 0 : num(0,s,mem);   
}
int num(int i, string &s, vector<int> &mem) {
    if(mem[i]>-1) return mem[i];
    if(s[i]=='0') return mem[i] = 0;
    int res = num(i+1,s,mem);
    if(i<s.size()-1 && (s[i]=='1'||s[i]=='2'&&s[i+1]<'7')) res+=num(i+2,s,mem);
    return mem[i] = res;
}

int main(){
    // string s = "123";
    // cout << s.substr(2,1) << endl;
    // cout << char(64+26) << endl;
    // cout << stoi("123") << endl;
    cout << numDecodings2("23") << endl; // 2
    cout << numDecodings2("1234") << endl; // 3
    cout << numDecodings2("12") << endl; // 2
    cout << numDecodings2("226") << endl; // 3
    cout << numDecodings2("0") << endl; // 0
    cout << numDecodings2("06") << endl; // 0
    cout << numDecodings2("111111111111111111111111111111111111111111111") << endl; // 0
}