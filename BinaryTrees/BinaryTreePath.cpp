/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        if(!root)
            return vector<string>{};
        if(!root->left && !root->right)
            return vector<string>{to_string(root->val)};
        
        auto leftTreePaths = binaryTreePaths(root->left);
        auto rightTreePaths = binaryTreePaths(root->right);
        for(auto& el : leftTreePaths)
            el = to_string(root->val)+"->"+el;
        for(auto& el : rightTreePaths)
            el = to_string(root->val)+"->"+el;
        
        leftTreePaths.insert(leftTreePaths.end(), make_move_iterator(rightTreePaths.begin()), make_move_iterator(rightTreePaths.end()));
        rightTreePaths.erase(rightTreePaths.begin(), rightTreePaths.end());
        
        return leftTreePaths;
    }
};
