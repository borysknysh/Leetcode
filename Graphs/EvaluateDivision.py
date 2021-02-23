class Solution:
    
    def dfs(self, current, end):
        if current in self.graph and end in self.graph:
            if current == end:
                return 1
            self.visited[current] = True
            for el in self.graph[current]:
                if self.visited[el[0]] == False:
                    ans = el[1] * self.dfs(el[0], end)
                    if ans != 0:
                        return ans
        
        return 0
    
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = defaultdict(list)
        self.weights = defaultdict(list)
        
        
        for el,w in zip(equations,values):
            self.graph[el[0]].append((el[1], w))
            self.graph[el[1]].append((el[0], 1./w))

        print(self.graph)
        
        res = []
        for sre, dst in queries:
            self.visited = {key: False for key in self.graph.keys()}
            ans = self.dfs(sre, dst)
            if ans == 0:
                ans = -1
            res.append(ans)
        
        return res
