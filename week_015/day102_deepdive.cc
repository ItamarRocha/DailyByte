/*
This question is asked by Google. Given an N-ary tree, return its maximum depth.
Note: An N-ary tree is a tree in which any node may have at most N children.

Ex: Given the following tree…

            4
          / | \
         3  9  2
        /       \
       7         2
return 3.
*/
#include <iostream>
#include <vector>

struct TreeNode {
    int val;
    std::vector<TreeNode*> childrens = {};
    TreeNode(int x) : val(x) {}
};
// Time O(n)
// Space O(n)
int max_depth(TreeNode* root){
    if(!root){
        return 0;
    }
    int max_depth_val = 0;
    for(int i = 0; i < root->childrens.size(); i++){
        max_depth_val = std::max(max_depth_val, max_depth(root->childrens[i]));
    }

    return max_depth_val + 1;
}

int main(){
    TreeNode root = TreeNode(4);
    TreeNode left = TreeNode(3);
    TreeNode middle = TreeNode(9);
    TreeNode right = TreeNode(2);
    TreeNode left_left = TreeNode(7);
    TreeNode right_right = TreeNode(2);
    root.childrens.push_back(&left);
    root.childrens.push_back(&right);
    root.childrens.push_back(&middle);
    left.childrens.push_back(&left_left);
    right.childrens.push_back(&right_right);

    std::cout << max_depth(&root) << std::endl;
}