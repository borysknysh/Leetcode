class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        visited = [[0]*n for _ in range(n)]
        res = [[0]*n for _ in range(n)]
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        nel = n**2
        
        i = j = 0
        v = 0
        for cntr in range(nel-1):
            res[i][j] = cntr+1
            visited[i][j] = 1
            if i + dr[v] < 0 or i + dr[v] >= n or j+dc[v] < 0 or j+dc[v] >= n or visited[i+dr[v]][j+dc[v]]:
                v = (v+1)%4
                
            i += dr[v]
            j += dc[v]
        res[i][j] = nel
        
        return res
