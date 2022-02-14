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
    vector<int> postorderTraversal(TreeNode* root) {
        if(!root)
            return vector<int>{};
        vector<int> temp;
        stack<TreeNode*> s;
        s.push(root);
        while(!s.empty())
        {
            auto curr = s.top();
            temp.push_back(curr->val);
            s.pop();
            if(curr->left)
                s.push(curr->left);
            if(curr->right)
                s.push(curr->right);
        }
        reverse(temp.begin(), temp.end());
        return temp;
    }
};
