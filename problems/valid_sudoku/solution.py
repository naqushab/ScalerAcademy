class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [set() for _ in range(len(board))]
        c = [set() for _ in range(len(board))]
        b = [set() for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                n = board[i][j]
                if n in r[i]:
                    return False
                r[i].add(n)
                
                if n in c[j]:
                    return False
                c[j].add(n)
                
                idx = (i//3)*3 + j//3
                if n in b[idx]:
                    return False
                b[idx].add(n)
        
        return True