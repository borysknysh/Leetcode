class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        lr = len(matrix)
        lc = len(matrix[0])
        visited = [[False] * lc for _ in matrix]
        
        r=c=i = 0
        ans = []
        for _ in range(lr*lc):
            ans.append(matrix[r][c])
            #print('up',matrix[r][c], r, c, i, dr[i], dc[i])
            visited[r][c] = True
            temp_r, temp_c = r+dr[i], c+dc[i]
            
            if 0 <= temp_r < lr and 0 <= temp_c < lc and not visited[temp_r][temp_c]:
                r,c = temp_r, temp_c
            else:
                i = (i+1)%4
                r, c = r+dr[i], c+dc[i]
                
        
        return ans
