class Solution {
public:
    int majorityElement(vector<int>& nums) {
        auto&& candidate = -1;
        auto&& cntr = 0;
        for(auto && el : nums)
        {
            if(cntr == 0)
                candidate = el;
            cntr += (candidate == el)?1:-1;
        }
        return candidate;
    }
};
