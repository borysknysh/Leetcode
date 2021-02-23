class Solution:        
    def hasCycle(self, v, visited, recStack, order):
        if visited[v] == False:
            visited[v] = True
            recStack[v] = True
            
            if v in self.graph:
                for el in self.graph[v]:
                    if ~visited[el] and self.hasCycle(el, visited, recStack, order):
                        return True
                    elif recStack[el]:
                        return True
            order.append(v)
            recStack[v] = False
            return False
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = {}
        
        for pair in prerequisites:
            if pair[0] not in self.graph:
                self.graph[pair[0]] = [pair[1]]
            else:
                self.graph[pair[0]].append(pair[1])
        
        visited = [False] * numCourses
        order = []
        recStack = [False]*numCourses
        for el in self.graph:
            if self.hasCycle(el, visited, recStack, order):
                return []
        for i in range(numCourses):
            if visited[i] == False:
                order = [i]+order
        return order
