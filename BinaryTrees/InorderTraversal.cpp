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
    void inorderTraversalUtil(TreeNode* root, vector<int>& result)
    {
        if(root == nullptr)
            return;
        inorderTraversalUtil(root->left, result);
        result.emplace_back(root->val);
        inorderTraversalUtil(root->right, result);    
    }
    vector<int> inorderTraversal(TreeNode* root) {
        // 1. inorder traversal of left tree
        // 2. root travesal
        // 3. inorder traversal of right tree
        vector<int> result;
        inorderTraversalUtil(root, result);
        
        return result;
    }
};
