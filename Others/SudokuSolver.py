class Solution:
    def find_empty(self, board: List[List[str]], l: List[str]) -> None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    l[0] = i
                    l[1] = j
                    return True
        return False
    def check_in_row(self, board: List[List[str]], row: List[str], num: str):
        for i in range(9):
            if board[row][i] == num:
                return True
        return False
        
    def check_in_col(self, board: List[List[str]], col: List[str], num: str):
        for i in range(9):
            if board[i][col] == num:
                return True
        return False
    def check_in_block(self, board: List[List[str]], row: List[str], col: List[str], num):
        for i in range(3):
            for j in range(3):
                if board[row+i][col+j] == num:
                    return True
        return False
    
    def check_valid(self, board: List[List[str]], row: List[str], col: List[str], num):
        return (not self.check_in_row(board, row, num)) and (not self.check_in_col(board, col, num)) and (not self.check_in_block(board, row-row%3, col-col%3, num))
    
    def solveSudokuUtil(self, board: List[List[str]]) -> None:
        l = [0,0]
        if not self.find_empty(board, l):
            return True
        row = l[0]
        col = l[1]
        for num in range(1,10):
            if self.check_valid(board, row, col, str(num)):
                board[row][col] = str(num)
                if self.solveSudokuUtil(board):
                    return True
                
                board[row][col] = '.'
        
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solveSudokuUtil(board)
        
