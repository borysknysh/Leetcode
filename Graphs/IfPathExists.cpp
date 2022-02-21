class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        // 1. Re-convert vector<vector<int>> to unordered_map<int, vector<int>>
        if(n == 1)
            return true;
        unordered_map<int, vector<int>> joins;
        for(const auto& el : edges)
        {
            joins[el[0]].push_back(el[1]);
            joins[el[1]].push_back(el[0]);
        }
        // 2. Define vector of visited vertices
        vector<bool> visited(n);
        
        // 3. Create DS to keep traversed graph elements and put there source element;
        stack<int> s;
        s.push(source);
        visited[source] = true;
        
        while(s.size())
        {
            auto&& last = s.top();
            s.pop();
            auto&& neighbours = joins[last];
            for(auto&& el : neighbours)
            {
                if(!visited[el])
                {
                    if(el == destination)
                        return true;
                    visited[el] = true;
                    s.push(el);
                }
            }
        }
        
        
        return false;
    }
};
