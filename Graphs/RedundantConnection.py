class Solution:    
    def findParent(self, parent, i):
        if parent[i] == -1:
            return i
        return self.findParent(parent, parent[i])
    def Union(self, parent, x, y):
        parent[x] = y
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
        self.graph = defaultdict(list)
        for el in edges:
            self.graph[el[0]].append(el[1])
            #self.graph[el[1]].append(el[0])
            
        print(self.graph)
        parent = (1+len(edges))*[-1]
        
        for el in edges:
                a = self.findParent(parent, el[0])
                print(a)
                b = self.findParent(parent, el[1])
                
                if a == b:
                    return el
                self.Union(parent, a, b)
            
