class Solution:
    
    def isCycle(self, v, recStack):
        if self.visited[v] == False:
            self.visited[v] = True
            recStack[v] = True
            if v in self.graph:
                for el in self.graph[v]:
                    if  (not self.visited[el]) and self.isCycle(el, recStack):
                        return True
                    elif recStack[el]:
                        return True
                
        recStack[v] = False
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #prerequisites = [[1,0],[0,1]]
        #numCourses = 2

        self.graph = {}
        self.visited = [False]*numCourses
        recStack = [False]*numCourses
        for el in prerequisites:
            if el[0] in self.graph:
                self.graph[el[0]].append(el[1])
            else:
                self.graph[el[0]] = [el[1]]
         
        for el in self.graph:
            if self.isCycle(el, recStack):
                return False
        return True
