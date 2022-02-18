class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        unordered_map<int, int> res;
        ++res[edges[0][0]];
        ++res[edges[0][1]];
        ++res[edges[1][0]];
        ++res[edges[1][1]];
        
        for(const auto& el : res)
            if(el.second == 2)
                return el.first;
        
        return -1;
    }
};
