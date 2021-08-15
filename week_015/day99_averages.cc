/*
This question is asked by Facebook. Given a reference to the root of a binary tree, 
return a list containing the average value in each level of the tree.

Ex: Given the following binary tree…

       1
      / \
    6    8
   / \ 
  1   5 
return [1.0, 7.0, 3.0]
*/

#include <vector>
#include <iostream>
#include <queue>
#include <map>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
// Time O(n)
// Space O(n)
vector<double> averages(TreeNode* root){
    queue<pair<TreeNode, int>> q;
    pair<TreeNode, int> node_level;
    map<int, pair<double,int>> map_count;

    q.push({*root, 0});
    int i = 0;
    while(!q.empty()){
        node_level = q.front();
        q.pop();

        if(map_count.find(node_level.second)== map_count.end()){
            map_count[node_level.second] = {0,0};
        }
        map_count[node_level.second].first += node_level.first.val;
        map_count[node_level.second].second += 1;

        if(node_level.first.left)
            q.push({*node_level.first.left, node_level.second+1});
        if(node_level.first.right)
            q.push({*node_level.first.right, node_level.second+1});
        i+=1;
        if( i >= 10)
            break;
    }
    vector<double> result;
    for(int i = 0; i < map_count.size(); i++){
        result.push_back((double)map_count[i].first / map_count[i].second);
    }
    return result;
}

vector<double> averages2(TreeNode* root){
    queue<TreeNode*> q;
    vector<double> result;
    q.push(root);
    
    while(!q.empty()){
        double sum = 0, count = 0;
        queue<TreeNode *> new_q;
        TreeNode* node;
        while(!q.empty()){
            node = q.front();
            q.pop();

            sum += node->val;
            count += 1;

            if(node->left)
                new_q.push(node->left);
            if(node->right)
                new_q.push(node->right);

        }
        result.push_back(sum/count);
        q = new_q;
        
    }
    return result;
}

// melhor desempenho no leetcode
vector<double> averages3(TreeNode* root){
    queue<TreeNode*> q;
    vector<double> result;
    double sum = 0, count = 0;
    int size;
    TreeNode* node;

    q.push(root);
    
    while(!q.empty()){
        size = q.size();
        sum = 0; count = 0;
        for(int i = 0; i < size; i++){
            node = q.front();
            q.pop();

            sum += node->val;
            count += 1;

            if(node->left)
                q.push(node->left);
            if(node->right)
                q.push(node->right);

        }
        result.push_back(sum/count);        
    }
    return result;
}

int main(){
    TreeNode root_left_left = TreeNode(1);
    TreeNode root_left_right = TreeNode(5);
    TreeNode root_left = TreeNode(6, &root_left_left, &root_left_right);
    TreeNode root_right = TreeNode(8);
    TreeNode root = TreeNode(-11, &root_left, &root_right);
    
    vector<double> result = averages3(&root);
    for(auto el: result)
        cout << el << " ";
}