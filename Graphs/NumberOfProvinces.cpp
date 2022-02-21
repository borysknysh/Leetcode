class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        auto&& n = (int)isConnected.size();
        vector<bool> visited(n, false);
        auto&& nLoops = 0;
        for(auto&& curr = 0; curr < n; ++curr)
        {
            if(visited[curr] == false)
            {
                stack<int> s;
                s.push(curr);
                visited[curr] = true;
                while(s.size())
                {
                    auto&& last = s.top();
                    s.pop();
                    vector<int> neighbours;
                    for(auto&& ne = 0; ne < n; ++ne)
                        if(isConnected[last][ne])
                        {
                            neighbours.push_back(ne);
                            /*if(!visited[ne])
                            {   
                                visited[ne] = true;
                                s.push(ne);
                            }*/
                        }
                    for(auto&& ne : neighbours)
                        if(!visited[ne])
                        {
                            visited[ne] = true;
                            s.push(ne);
                        }
                }
                ++nLoops;
            }
        }
        return nLoops;
    }
};
