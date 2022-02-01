class Solution:
	# @param A : tuple of strings
	# @return an integer
    def isValidSudoku(self, A):
        N = len(A)
        row = [set() for _ in range(N)]
        col = [set() for _ in range(N)]
        block = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                v = A[r][c]
                if v == '.':
                    continue
                if v in row[r]:
                    return 0
                row[r].add(v)
                if v in col[c]:
                    return 0
                col[c].add(v)
                idx = self.get_block_index(r, c)
                if v in block[idx]:
                    return 0
                block[idx].add(v)
        return 1
    
    def get_block_index(self, r, c):
        if r <3 and c < 3:
            return 0
        elif r < 3 and 3<= c< 6:
            return 1
        elif r<3 and 6<=c<9:
            return 2
        elif 3<=r <6 and c < 3:
            return 3
        elif 3<=r <6 and 3<= c< 6:
            return 4
        elif 3<=r <6 and 6<=c<9:
            return 5
        elif 6<=r <9 and c < 3:
            return 6
        elif 6<=r <9 and 3<= c< 6:
            return 7
        elif 6<=r <9 and 6<=c<9:
            return 8