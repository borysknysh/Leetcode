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
    int maxDepth(TreeNode* root) {
        // if root is null, maxdepth is zero;
        // 1. Find max depth of left subtree;
        // 2. Find max depth of right subtree;
        // 3. Add 1 to highest of those;
        
        if(!root)
            return 0;
        auto maxDepthOfLeftSubTree = maxDepth(root->left);
        auto maxDepthOfRightSubTree = maxDepth(root->right);
        auto maxDepthTotal = (maxDepthOfLeftSubTree >= maxDepthOfRightSubTree) ? maxDepthOfLeftSubTree:maxDepthOfRightSubTree;
        return maxDepthTotal+1;
    }
};
