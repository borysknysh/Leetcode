class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        if(n == 1 and trust.size()==0)
            return 1;
        unordered_map<int, int> t;
        for(const auto& el : trust)
            ++t[el[0]];
        if(t.size() == n)
            return -1;
        unordered_map<int, int> tt;
        for(const auto& el : trust)
            ++tt[el[1]];
        
        for(auto&& i = 1; i <= n; ++i)
            if( (t.find(i) == t.end()) && (tt.find(i) != tt.end()) && (tt[i] == n-1) )
                return i;
        return -1;
    }
};
