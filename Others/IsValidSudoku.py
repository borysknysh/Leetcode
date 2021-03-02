class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashTemp = defaultdict(bool)
        length = len(board)
        
        for i in range(length):
            for j in range(length):
                if board[i][j] != '.':
                    if board[i][j] in hashTemp:
                        return False
                    hashTemp[board[i][j]] = True
            hashTemp = defaultdict(bool)
        
        for i in range(length):
            for j in range(length):
                if board[j][i] != '.':
                    if board[j][i] in hashTemp:
                        return False
                    hashTemp[board[j][i]] = True
            hashTemp = defaultdict(bool)
        for qi in range(3):
            for qj in range(3):
                for i in range(3*qi, 3*(qi+1), 1):
                    for j in range(3*qj, 3*(qj+1), 1):
                        if board[j][i] != '.':
                            if board[j][i] in hashTemp:
                                return False
                            hashTemp[board[j][i]] = True
                hashTemp = defaultdict(bool)
        
        return True
