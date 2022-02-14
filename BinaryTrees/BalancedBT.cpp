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
    bool isBalancedUtil(TreeNode* root, int& height)
    {
        if(!root)
        {
            height = 0;
            return true;
        }
        auto&& leftHeight = 0;
        auto&& rightHeight = 0;
        
        auto&& isLeftBalanced = isBalancedUtil(root->left, leftHeight);
        auto&& isRightBalanced = isBalancedUtil(root->right, rightHeight);
        height = 1 + ((leftHeight <= rightHeight) ? rightHeight:leftHeight);
        return isLeftBalanced && isRightBalanced && abs(leftHeight-rightHeight) <= 1;
    }
    bool isBalanced(TreeNode* root) {
        auto&& height = 0;
        // The tree is balanced, when left and right parts are balanced and heights difference between left and right subtrees is <= 1.
        return isBalancedUtil(root, height);
    }
};
