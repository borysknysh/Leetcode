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
    bool isSymmetricUtil(TreeNode* p, TreeNode* q)
    {
        if(p != nullptr && q != nullptr)
            return p->val == q->val && isSymmetricUtil(p->left, q->right) && isSymmetricUtil(p->right, q->left);
        else if(p == nullptr && q == nullptr)
            return true;
        else
            return false;
    }
    bool isSymmetric(TreeNode* root) {
        return isSymmetricUtil(root->left, root->right);
    }
};
