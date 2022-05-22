class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return
        
        def solve():        
            for i, j in itertools.product(range(n), range(n)):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        num_str = str(num)
                        if is_valid(board, i, j, num_str):
                            board[i][j] = num_str
                            if solve():
                                return True
                            else:
                                board[i][j] = '.'
                    return False
            return True
                        
        def is_valid(board, r, c, num):
            for i in range(9):
                if board[i][c] != '.' and board[i][c] == num:
                    return False
                if board[r][i] != '.' and board[r][i] == num:
                    return False
                if board[3*(r//3) + i//3][3*(c//3) + i%3] != '.' and board[3*(r//3)+i//3][3*(c//3) + i%3] == num:
                    return False
            return True
        
        solve()
        return