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
    TreeNode* sortedArrayToBSTUtil(vector<int>& nums, const int& l, const int& r)
    {
        if(l>r)
            return nullptr;
        if(l == r)
        {
            return new TreeNode(nums[l]);
        }
        auto&& length = r-l+1;
        //cout << l+length/2 << "  " << nums.size() << '\n';
        auto&& median = nums[l+length/2];
        
        auto leftBST = sortedArrayToBSTUtil(nums,l,l+length/2-1);
        auto rightBST = sortedArrayToBSTUtil(nums, l+length/2+1, r);
        return new TreeNode(median, leftBST, rightBST);
    }
    
    TreeNode* sortedArrayToBST(vector<int>& nums)
    {
        auto&& length = int(nums.size());
        return sortedArrayToBSTUtil(nums, 0, length-1);
    }
};
