class Solution:
    # O(N)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
        #n =6
        
        if n <= 2:
            return [el for el in range(n)]
        
        graph = defaultdict(list)
        
        for el in edges:
            graph[el[0]].append(el[1])
            graph[el[1]].append(el[0])
            
        leaves = []
        for el in graph:
            if len(graph[el]) == 1:
                leaves.append(el)
        
        total = len(graph)
        while total > 2:
            new_leaves = []
            total -= len(leaves)
            while leaves:
                leaf = leaves.pop()
                #print(graph)
                neighbor = graph[leaf].pop()
                del graph[leaf]
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
        
        
    #### O(N^2)
    #def pathL(self, v, vertices, recCntr):
    #    vertices[v] = True
    #    recCntr += 1
    #    for el in self.graph[v]:
    #        if vertices[el] == False:
    #            self.pathL(el, vertices, recCntr)
    #    if recCntr > self.maxDepth:
    #        self.maxDepth = recCntr 
    #    recCntr -= 1 
    #    
    #def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #    #edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
    #    #n = 6
    #    
    #    if len(edges) == 0:
    #        return [el for el in range(n)]
    #    
    #    self.graph = defaultdict(list)
    #    
    #    for el in edges:
    #        self.graph[el[0]].append(el[1])
    #        self.graph[el[1]].append(el[0])
    #    
    #    vertices = [False]*n
    #    self.maxDepth = 0
    #    mih = {}
    #    absolute_min = n
    #    for el in self.graph:
    #        vertices = [False]*n
    #        self.maxDepth = 0
    #        recCntr = 0
    #        self.pathL(el, vertices, recCntr)
    #        mih[el] = self.maxDepth
    #        if self.maxDepth < absolute_min:
    #            absolute_min = self.maxDepth
    #    return [el for el in mih if mih[el]==absolute_min]
