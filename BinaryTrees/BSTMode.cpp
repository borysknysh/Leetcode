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
    void inorderTraversal(TreeNode* root, unordered_map<int, int>& res, int& maxCntr)
    {
        if(!root)
            return;
        inorderTraversal(root->left, res, maxCntr);
        maxCntr = max(maxCntr, ++res[root->val]);
        inorderTraversal(root->right, res, maxCntr);
    }
        
    vector<int> findMode(TreeNode* root) {
        auto&& currCntr = 0;
        auto&& maxCntr = 0;
        unordered_map<int, int> res;
        inorderTraversal(root, res,  maxCntr);
        vector<int> mode;
        for(auto&& el : res)
            if(el.second == maxCntr)
                mode.push_back(el.first);
        return mode;
    }
};
